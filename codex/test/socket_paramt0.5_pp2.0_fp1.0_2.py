import socket
socket.if_indextoname(1)

# get all interfaces
for i in range(1,100):
    try:
        name = socket.if_indextoname(i)
        print(name)
    except:
        print("error")

# get IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

# get MAC address
import uuid
mac = uuid.getnode()
mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
print(mac)
