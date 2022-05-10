import socket
# Test socket.if_indextoname() on some interfaces.
for i in [1, 2, 3, 4]:
    try:
        print(socket.if_indextoname(i))
    except:
        pass

# Test socket.if_indextoname() on invalid interface.
try:
    print(socket.if_indextoname(5))
except:
    print('invalid interface 5')
