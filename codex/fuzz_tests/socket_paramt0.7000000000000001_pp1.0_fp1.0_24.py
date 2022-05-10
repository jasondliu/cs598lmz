import socket
socket.if_indextoname(socket.if_index(interface))

ip = get_ip_address(interface)
print(ip)

from uuid import getnode as get_mac
mac = get_mac()
print(mac)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

is_connected()

import datetime
now = datetime.datetime.now()
a = now.strftime("%Y%m%d%H%M%S")
print(a)
