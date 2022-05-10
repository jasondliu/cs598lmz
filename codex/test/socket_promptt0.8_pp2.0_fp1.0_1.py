import socket
# Test socket.if_indextoname(if_index)
NIC_NAME = 'eth0'
if_index = socket.if_nametoindex(NIC_NAME)
print('{} index is {}'.format(NIC_NAME, if_index))

# Test socket.if_indextoname(if_index)
print('{} name is {}'.format(if_index, socket.if_indextoname(if_index)))

# Test socket.if_nameindex()
NIC_NAME_LIST = socket.if_nameindex()
for name_index in NIC_NAME_LIST:
    print('{} name is {}'.format(name_index[0], name_index[1]))

# Test socket.if_nametoindex(NIC_NAME)
for name_index in NIC_NAME_LIST:
    name = name_index[1]
    if_index = socket.if_nametoindex(name)
    print('{} index is {}'.format(name, if_index))

# Test socket.if_nameindex()
