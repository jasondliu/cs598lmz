import socket
# Test socket.if_indextoname()

for i in range(10):
    try:
        name = socket.if_indextoname(i)
        print(f'{i}: {name}')
    except OSError:
        print(f'{i}: not found')
