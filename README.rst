======
remot3
======


.. image:: https://img.shields.io/pypi/v/remot3.svg
        :target: https://pypi.python.org/pypi/remot3

.. image:: https://img.shields.io/travis/twaclaw/remot3.svg
        :target: https://travis-ci.com/twaclaw/remot3

.. image:: https://readthedocs.org/projects/remot3/badge/?version=latest
        :target: https://remot3.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/twaclaw/remot3/shield.svg
     :target: https://pyup.io/repos/github/twaclaw/remot3/
     :alt: Updates



Implementation of the remot3.it API


* Free software: MIT license
* Documentation: https://remot3.readthedocs.io.


Features
--------

Installation
~~~~~~~~~~~~~

.. code:: bash
        
        pip install remot3

Usage 
~~~~~

.. code-block:: Python

        from remot3 import remot3

        r3 = Remot3(developer_key, user, password)

        # Optionally, the api version can be defined
        r3 = Remot3(developer_key, user, password, apiurl='https://api.remot3.it/apv/v27/')

        r3.login()

        # A complete list of the devices can be retrieved, or
        status,  devices, _ = r3.list_devices()

        # Given an installation name retrieve the connection parameters
        devices = r3.get_device_address(deviceName='MyDeviceName', serviceType='SSH')
        if len(devices) > 0:
                status, proxyserver, proxyport,  _ = r3.get_server_name(devices[0])
                print('ssh user@{} -p {}'.format(proxyserver, proxyport))
        

Credits
-------

* https://remote.it/

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
        .. _Cookiecutter: https://github.com/audreyr/cookiecutter
        .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
