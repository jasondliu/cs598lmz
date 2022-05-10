import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
for if_index, name in socket.if_nameindex():
    print('({}) {}'.format(if_index, name))

# if_nameindex() - DNS queries
for if_index, name in socket.if_nameindex():
    if_name = socket.if_indextoname(if_index)
    # Query interface IP addr
    try:
        packed = socket.inet_aton(socket.INADDR_ANY)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(
            socket.SOL_SOCKET, socket.SO_BINDTODEVICE, if_name
        )
        s.connect((socket.inet_ntoa(packed), 1234))
        print("{}: {}".format(name, s.getsockname()[0]))
    except:
        print("{}".format(name), 'is down')
    finally:
       
