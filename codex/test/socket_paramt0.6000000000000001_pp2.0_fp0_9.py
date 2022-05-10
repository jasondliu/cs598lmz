import socket
socket.if_indextoname(3)

# 使用ip_address()类来获取IP地址
from ipaddress import ip_address
ip_address('192.168.0.1')
ip_address('2001:db8::')

# 使用ip_network()类来创建IP网络
from ipaddress import ip_network
ip_network('2001:db8::/32')
ip_network('192.168.0.0/24')

# 使用ip_interface()类来获取接口的IP地址
from ipaddress import ip_interface
ip_interface('192.168.0.1/24')
ip_interface('2001:db8::/32')

# 使用hostname_types.DNSLabel类来创建DNS标签
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
