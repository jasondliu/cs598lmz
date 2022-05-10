import socket
# Test socket.if_indextoname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(0, 10):
    name = s.if_indextoname(i)
    print 'Index %d = %s' % (i, name)
