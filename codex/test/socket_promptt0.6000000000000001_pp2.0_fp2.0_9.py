import socket
# Test socket.if_indextoname
for index in range(0,10):
    try:
        name = socket.if_indextoname(index)
        print(name)
    except:
        continue

# Test socket.if_nameindex
for name, index in socket.if_nameindex():
    print(name, index)

# Test socket.if_nametoindex
for index in range(0,10):
    try:
        name = socket.if_nametoindex(socket.if_indextoname(index))
        print(index, name)
    except:
        continue

# Test socket.if_indextoname
for index in range(0,10):
    try:
        name = socket.if_indextoname(index)
        print(index, name)
    except:
        continue
