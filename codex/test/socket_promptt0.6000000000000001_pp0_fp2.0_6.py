import socket
# Test socket.if_indextoname()

for i in range(64):
    try:
        print(socket.if_indextoname(i))
    except ValueError:
        print('ValueError')
    except OSError:
        print('OSError')
