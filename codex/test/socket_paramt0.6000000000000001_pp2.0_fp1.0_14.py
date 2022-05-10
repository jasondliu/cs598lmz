import socket
socket.if_indextoname(1)

#ifconfig
#ifconfig en0

# ifconfig en0 | grep 'inet ' | cut -d' ' -f2

import netifaces
for interface in netifaces.interfaces():
    print(interface)
    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
        print(link)

# import netifaces
# for interface in netifaces.interfaces():
#     print(interface)
#     for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
#         print(link)

# import netifaces
# for interface in netifaces.interfaces():
#     print(interface)
#     for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
#         print(link)


import netifaces

# print(netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr'])

import netifaces

