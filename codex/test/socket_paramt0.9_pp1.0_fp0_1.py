import socket
socket.if_indextoname("1")
# 'en0'

import netifaces
netifaces.interfaces()
# ['en0', 'lo0', 'gif0', 'stf0']

netifaces.ifaddresses('en0')
# {2: [{'addr': 'fe80::68de:64ff:fee8:57a',
#       'netmask': 'ffff:ffff:ffff:ffff::'}],
#  17: [{'addr': 'fe80::68de:64ff:fee8:57a%en0',
#        'netmask': 'ffff:ffff:ffff:ffff::'}],
#  18: [{'addr': '2601:602:8970:97bc:68de:64ff:fee8:57a0',
#        'netmask': 'ffff:ffff:ffff:ffff::'}],
#  30: [{'addr': 'fe80::4c4f:4bff:fe5a:d6e5%utun1',
#        'netmask': 'ffff:ffff:ffff:ffff::'},
