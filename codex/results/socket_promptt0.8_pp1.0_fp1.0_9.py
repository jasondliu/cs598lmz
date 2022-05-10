import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except OSError as e:
    if e.args[0] == 95:
        print('SKIP')
        raise SystemExit

import uos

def ifc_info(ifname, ifcinfo):
    print('%-10s: %d' % (ifname, ifcinfo[0]))

print("ifconfig():")
for ifname, ifcinfo in uos.ifconfig().items():
    ifc_info(ifname, ifcinfo)

# Note: on OS X, it appears that no interface is returned
# when not running as root.
if uos.geteuid() == 0:
    print("ifc_info():")
    for interface in uos.uname().interfaces:
        ifc_info(interface, uos.ifc_info(interface))
