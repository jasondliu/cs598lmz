import socket
socket.if_indextoname('1')

client.ifconfig('lo0', up=True)
client.print_function_list('link')
client.link('lo0')
client.print_function_list('netlink')
client.netlink('lo0')

client.set('lo0')
s = client.get('lo0')
s.ipv4_address
s.name
s.operstate
s.mac
s.mtu
s.link_info.txqlen
client.set('lo0.txqlen', 100)
client.get('lo0.txqlen')

from os import name as os_name
from platform import system as platform_system
if os_name == 'posix' and platform_system() == 'Linux':
    client.set('eth0')
    s.propagate_uplink()

from pyroute2 import IPRoute
ip = IPRoute()
