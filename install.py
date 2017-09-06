# installer for the weatherflow-udp driver
# Copyright 2017 Arthur Emerson, vreihen@yahoo.com
# Distributed under the terms of the GNU Public License (GPLv3)

from setup import ExtensionInstaller

def loader():
    return WeatherFlowUDPInstaller()

class WeatherFlowUDPInstaller(ExtensionInstaller):
    def __init__(self):
        super(WeatherFlowUDPInstaller, self).__init__(
            version="0.10",
            name='weatherflowudp',
            description='Capture data from WeatherFlow Bridge via UDP broadcast packets',
            author="Arthur Emerson",
            author_email="vreihen@yahoo.com",
            files=[('bin/user', ['bin/user/weatherflowudp.py'])]
            )

