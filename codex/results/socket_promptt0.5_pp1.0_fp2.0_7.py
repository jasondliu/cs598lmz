import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    if_index = 1
    print(socket.if_indextoname(if_index))
