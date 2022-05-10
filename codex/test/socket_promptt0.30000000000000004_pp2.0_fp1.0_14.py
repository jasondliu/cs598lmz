import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform[:3] == 'win':
    print('\nWindows platform, skipping test\n')
    sys.exit(0)

# get a list of all network interfaces on this host
import netifaces

ifaces = netifaces.interfaces()

# print the name of each interface
for ifname in ifaces:
    print('%s:' % ifname)
    # get the address(es) of each interface
    addrs = netifaces.ifaddresses(ifname)
    # print the address(es) of each interface
    for addrtype in addrs.keys():
        for addr in addrs[addrtype]:
            print('  %s: %s' % (addrtype, addr))

# get the index of the interface named 'lo'
lo_index = socket.if_nametoindex('lo')

# get the name of the interface with index 1
ifname = socket.if_indextoname(lo_index)

