import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: if_indextoname.py <ifindex>')
        sys.exit(2)
    ifindex = int(sys.argv[1])
    print(socket.if_indextoname(ifindex))
