======
remot3
======

.. image:: https://img.shields.io/pypi/v/remot3.svg
        :target: https://pypi.python.org/pypi/remot3

.. image:: https://img.shields.io/pypi/l/remot3.svg
        :target: https://pypi.python.org/pypi/remot3

.. image:: https://img.shields.io/pypi/pyversions/remot3.svg
        :target: https://pypi.python.org/project/remot3


A simple implementatoin of the remot3.it API


* Free software: MIT license
* Documentation: https://remot3.readthedocs.io.


Installation
~~~~~~~~~~~~~

.. code:: bash
        
        pip install remot3

Usage 
~~~~~

.. code-block:: Python

        from remot3 import remot3

        r3 = Remot3(developer_key, user, password)

        # Optionally, the api version can be specified
        r3 = Remot3(developer_key, user, password, apiurl='https://api.remot3.it/apv/v27/')

        r3.login()

        # Get the list of all devices
        status,  devices, _ = r3.list_devices()

        # Retrieve the connection parameters for one particular connection: MyDeviceName
        devices = r3.get_device_address(deviceName='MyDeviceName', serviceType='SSH')
        if len(devices) > 0:
                status, proxyserver, proxyport,  _ = r3.get_server_name(devices[0])
                print('ssh user@{} -p {}'.format(proxyserver, proxyport))
        

Credits
-------

- https://remot3.it/
- This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template
        .. _Cookiecutter: https://github.com/audreyr/cookiecutter
        .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
