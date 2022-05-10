import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    if_name = socket.if_indextoname(1)
    print(if_name)
