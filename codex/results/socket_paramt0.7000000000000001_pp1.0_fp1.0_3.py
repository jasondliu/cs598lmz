import socket
socket.if_indextoname(0x00000005), socket.if_indextoname(0x00000005).encode()

#import netifaces
#netifaces.interfaces()
#netifaces.ifaddresses('en0')
#netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
#netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']

#import pyaudio
#pa = pyaudio.PyAudio()
#[pa.get_device_info_by_index(i) for i in range(pa.get_device_count())]
#pa.get_device_info_by_index(5)['name']

#import uuid
#uuid.uuid1()
#uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')

#import os
#os.getlogin()

#import platform
#platform.platform()
#platform.architecture()
#platform.machine()
#platform.node
