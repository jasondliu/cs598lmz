import socket
# Test socket.if_indextoname

NIC_NAME = 'lo'

if_index = socket.if_nametoindex(NIC_NAME)
if_name = socket.if_indextoname(if_index)

print(if_name)
if if_name != NIC_NAME:
    print('Error: socket.if_indextoname failed')
