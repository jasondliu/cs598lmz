import socket
# Test socket.if_indextoname()
print socket.if_indextoname(8)
print socket.if_indextoname(7)

# Test ipaddress._islinklocal()
from ipaddress import ip_address, _is_integer
print ip_address('202.124.2.192')
print ip_address('202.124.2.192') > ip_address('202.124.2.0')
print ip_address('202.124.2.192') <= ip_address('202.124.2.255')
print ip_address('202.124.2.192') >= ip_address('202.124.2.0')
print ip_address('202.124.2.192') < ip_address('202.124.2.255')


# Test struct.pack()
from struct import pack
print pack('4s4s4s4s4s4s4s4s', '\x00\x00\x00\x00','\x00\x00\x00\x00','\x00\x00\x00\x00','\x00\x00\x
