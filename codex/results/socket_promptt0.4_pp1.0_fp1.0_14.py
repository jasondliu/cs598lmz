import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(s.if_indextoname(1))
    print(s.if_indextoname(2))
    print(s.if_indextoname(3))
    print(s.if_indextoname(4))
    print(s.if_indextoname(5))
    print(s.if_indextoname(6))
