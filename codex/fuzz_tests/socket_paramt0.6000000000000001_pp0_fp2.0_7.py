import socket
socket.if_indextoname('12')

import netifaces
netifaces.ifaddresses('en0')
netifaces.ifaddresses('en0')[netifaces.AF_LINK]
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']
netifaces.interfaces()

import uuid
[i for i in dir(uuid) if not i.startswith('_')]
uuid.getnode()
uuid.getnode() >> 40
hex(uuid.getnode())

import os
os.urandom(6)

import hashlib
hashlib.md5(os.urandom(6)).hexdigest()

import platform
platform.platform()
platform.node()
platform.processor()
