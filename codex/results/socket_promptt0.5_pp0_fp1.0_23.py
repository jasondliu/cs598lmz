import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    try:
        print(socket.if_indextoname(0))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(32))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(1))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(2))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(3))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(4))
    except OSError:
        print("OSError")
    try:
        print(socket.if_indextoname(5))
    except OSError:
        print("OSError")
    try:
