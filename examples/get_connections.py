# -*- coding: utf-8 -*-

"""Prints the remot3.it ssh proxy and port for the selected installation

The script lists the existing installations and retrieves the connection params 
for the one selected by the user.
"""

import os
import sys

import click
from remot3 import Remot3

_DEVELOPER_KEY = os.environ["R3_DEVELOPER_KEY"] if 'R3_DEVELOPER_KEY' in os.environ else None
_USER = os.environ["R3_USER"] if 'R3_USER' in os.environ else None
_PASSWORD = os.environ["R3_PASSWORD"] if 'R3_PASSWORD' in os.environ else None


@click.command()
@click.option('--user', default='', help='remot3.it user')
@click.option('--password', default='', help='remot3.it password')
@click.option('--developer_key', default='', help='remot3.it developper key')
def connect(user, password, developer_key):
    if not user:
        user = _USER

    if not password:
        password = _PASSWORD
    
    if not developer_key:
        developer_key = _DEVELOPER_KEY
    
    r3 = Remot3(developer_key, user, password, apiurl='https://api.remot3.it/apv/v27/')
    status, response = r3.list_devices()

    if status != 200 or not response['status']:
        print("Error while listing devices: requests_status: {}, \
               response: {}".format(status, response))
        sys.exit(-2)

    # list devices with SSH service
    devices = response['devices']
    index = 0
    ssh_devices = []
    for d in devices:
        service = d['servicetitle']
        if service == 'SSH':
            ssh_devices.append(d)
            print('{} : {}'.format(index, d['devicealias']))
            index += 1

    value = -1
    while value < 0 or value >= index:
        value = click.prompt(
            'Please select an installation [0-{}]'.format(index - 1), default=0)

    deviceAddr = ssh_devices[value]['deviceaddress']
    deviceName = ssh_devices[value]['devicealias']

    print('\nConnecting to device: {} with address: {}'.format(
        deviceName, deviceAddr))

    proxyserver, proxyport = r3.get_server_name(deviceAddr)

    print('='*30)
    print('\nssh commands:')
    print('='*30)
    print('ssh pi@{} -p {} # Normal ssh connection'.format(
        proxyserver, proxyport))
    print('ssh pi@{} -p {} -D 8080 # Dynamic port forwarding'.format(
        proxyserver, proxyport))

    print()
    ip = click.prompt(
        'If required, enter the target heat pump ip address',
        default='')

    if ip:
        print('='*30)
        print('\nssh commands:')
        print('='*30)
        print('ssh pi@{} -p {} -L 8080:{}:80 # Forward port 80 to localhost:8080'.format(
            proxyserver, proxyport, ip))
        print('ssh pi@{0} -p {1} -L 80:{2}:80 -L 1131:{2}:1131 -L 51705:{2}:51705 -L 52533:{2}:52533\
                # For remote debug with c.suite'.format(
            proxyserver, proxyport, ip))


if __name__ == "__main__":
    connect()
