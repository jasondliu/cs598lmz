import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    for i in range(10):
        try:
            print(socket.if_indextoname(i))
        except OSError:
            pass
