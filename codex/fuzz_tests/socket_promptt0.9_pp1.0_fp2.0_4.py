import socket
# Test socket.if_indextoname is implemented.
try:
    _soc = socket.socket()
    _soc.bind((socket.if_indextoname(-1), 0))
except OverflowError as e:
    pass
print('if_indextoname: OK')
# Test socket.if_nameindex is implemented.
socket.if_nameindex()
print('if_nameindex: OK')
