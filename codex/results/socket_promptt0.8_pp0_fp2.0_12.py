import socket
# Test socket.if_indextoname
def if_indextoname(index):
    try:
        name = socket.if_indextoname(index)
        print('if_indextoname({}) => {}'.format(index, name))
    except ValueError as err:
        print('if_indextoname({}) => {}'.format(index, err))

if_indextoname(0)
if_indextoname(1)
if_indextoname(1000)
