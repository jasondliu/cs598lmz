import socket
# Test socket.if_indextoname()
for i in range(10):
    try:
        print(socket.if_indextoname(i))
    except ValueError:
        pass
</code>

