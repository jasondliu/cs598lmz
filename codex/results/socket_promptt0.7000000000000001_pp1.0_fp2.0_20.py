import socket
# Test socket.if_indextoname()
for i in range(10):
    try:
        name = socket.if_indextoname(i)
        print('%d->%s' % (i, name))
    except Exception as e:
        print(e)
