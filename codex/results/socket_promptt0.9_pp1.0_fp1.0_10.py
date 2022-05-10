import socket
# Test socket.if_indextoname and socket.if_nametoindex -
# this assumes one or more interfaces are up and running
if_names = [socket.if_indextoname(i) for i in range(256)]
if_name_bad = socket.if_indextoname(-1)
if_indices = [socket.if_nametoindex(n) for n in if_names]
if_index_bad = socket.if_nametoindex('ABCDEFGHIJKLMNOP')

failed_heritage = []
for i, (n1, n2, i2) in enumerate(zip(if_names, if_names[1:], if_indices[1:])):
    if i2 != i + 1:
        failed_heritage.append('FAILED: index %d: if_nametoindex(%s) returned '
            '%d rather than %d' % (i + 1, n1, i2, i + 1))
    if n2 != socket.if_indextoname(i2):
        failed_heritage.append('FAILED: name
