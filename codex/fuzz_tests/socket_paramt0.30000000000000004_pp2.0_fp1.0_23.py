import socket
socket.if_indextoname(3)

# get the IP address of the interface
import socket
socket.if_nameindex()

# get the MAC address of the interface
import uuid
print(hex(uuid.getnode()))

# get the MAC address of the interface
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

# get the MAC address of the interface
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

# get the MAC address of the interface
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

# get the MAC address of the interface
import uuid
