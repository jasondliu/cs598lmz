import socket
# Test socket.if_indextoname()
for if_index in range(10):
    try:
        if_name = socket.if_indextoname(if_index)
    except ValueError:
        if_name = None
    print '%d: %s' % (if_index, if_name)

# Test socket.if_nameindex()
if_index_map = socket.if_nameindex()
for if_index, if_name in if_index_map:
    print '%d: %s' % (if_index, if_name)
