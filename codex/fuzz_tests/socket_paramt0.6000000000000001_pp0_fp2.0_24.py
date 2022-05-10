import socket
socket.if_indextoname(3)

#import netifaces
#netifaces.ifaddresses('eth0')

import os
os.system('ifconfig')

#import subprocess
#subprocess.call(['ifconfig'])

#import commands
#print commands.getoutput('ifconfig')

#import os, sys
#if sys.platform == 'win32':
#    print os.popen('ipconfig').read()
#else:
#    print os.popen('ifconfig').read()

#from netifaces import interfaces, ifaddresses, AF_INET
#for ifaceName in interfaces():
#    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
#    print '%s: %s' % (ifaceName, ', '.join(addresses))
