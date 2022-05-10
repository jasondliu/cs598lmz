import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(2)
except OSError as e:
    print(f'[FAIL]: {type(e)} {e}')

try:
    socket.if_indextoname(1)
except OSError as e:
    print(f'[FAIL]: {type(e)} {e}')

print(f'{type(socket.if_indextoname(3))} {socket.if_indextoname(3)}')
print('[SUCCESS]')
