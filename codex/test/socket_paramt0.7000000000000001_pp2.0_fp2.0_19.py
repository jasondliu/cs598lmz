import socket
socket.if_indextoname(3)

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('lo')
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('eth1')

import re
import os
import platform

#print(os.name)
print(platform.system())
print(platform.release())

if re.match('(.*)Windows(.*)', platform.system()):
    print('\nThis is a Windows system.')
    print(platform.win32_ver())
    p = platform.win32_ver()
    ver = p[0]
    if re.match('(.*)10(.*)', ver):
        print('\nThis is Windows 10.')
    elif re.match('(.*)8(.*)', ver):
        print('\nThis is Windows 8.')
    elif re.match('(.*)7(.*)', ver):
        print('\nThis is Windows 7.')
