# -*- coding: utf-8 -*-

"""Prints a remot3 ssh proxy and port for a given installation

The script lists the existing installations and retrieves the 
ssh connection parameters for the one selected by the user.
"""

import os
import click

from remot3 import Remot3


# The API connection params can be defined as env variables 
# or passed as command line arguments

_DEVELOPER_KEY = os.environ["R3_DEVELOPER_KEY"] \
     if 'R3_DEVELOPER_KEY' in os.environ else None
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
    r3.login()

    # A complete list of the devices can be retrieved, or
    status,  devices, _ = r3.list_devices()

    # Given an installation name retrieve the connection parameters
    devices = r3.get_device_address(deviceName='MyDeviceName', serviceType='SSH')
    if len(devices) > 0:
        status, proxyserver, proxyport,  _ = r3.get_server_name(devices[0])
        print('ssh user@{} -p {}'.format(proxyserver, proxyport))
 

if __name__ == "__main__":
    connect()
