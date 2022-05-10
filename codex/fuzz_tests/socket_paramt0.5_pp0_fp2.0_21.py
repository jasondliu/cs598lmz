import socket
socket.if_indextoname(3)

# get all interfaces
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
max_possible = 8 # initial value
while True:
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE,
                     struct.pack('256s', bytes(str(max_possible), 'utf-8')))
        max_possible += 1
    except:
        break

interfaces = [socket.if_indextoname(i) for i in range(max_possible)]
interfaces.remove('lo')

# get all ipv4 addresses
ip_list = []
for i in interfaces:
    if i == 'lo':
        continue
    ip_list.append(socket.gethostbyname(i))

# get all ipv6 addresses
ip6_list = []
for i in interfaces:
    if i == 'lo':
        continue
    ip6_list.append(socket.getaddrinfo(i, 0, socket.AF_
