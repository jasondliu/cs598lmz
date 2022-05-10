import socket
socket.if_indextoname(3)

# 'en0'
# or

import netifaces
netifaces.ifaddresses('en0')

# {
#     17: [{
#         'addr': '01:02:03:04:05:06',
#         'broadcast': 'ff:ff:ff:ff:ff:ff'
#     }],
#     2: [{
#         'addr': '192.168.1.101',
#         'netmask': '255.255.255.0',
#         'broadcast': '192.168.1.255'
#     }]
# }
