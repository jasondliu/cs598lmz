import socket
socket.if_indextoname(int(open('/sys/class/net/eth0/ifindex').read()))

 

import socket

### Detect if we're running on kvm
import re
def is_kvm():
    kvm = False
    for i in range(4):
        with open('/sys/class/net/eth%d/address' % i, 'r') as fd:
            mac = fd.readline()
            if re.match(r'52:54:00:', mac):
                return True
    return False

# This is the client (local) socket
client = socket.socket(socket.AF_UNIX,
                       socket.SOCK_DGRAM, 0)

if is_kvm():
    client.connect('/tmp/openswitch-vswitchd')
else:
    client.connect('/var/run/openswitch-vswitchd')

# This is the management socket
management = socket.socket(socket.AF_UNIX,
                           socket.SOCK_DGRAM, 0)

if is_kvm():
   
