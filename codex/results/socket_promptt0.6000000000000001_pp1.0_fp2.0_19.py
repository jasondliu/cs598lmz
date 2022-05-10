import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    if not hasattr(socket, 'if_indextoname'):
        print('SKIP')
        raise SystemExit

    # get the interface index for 'lo'
    for i in socket.if_nametoindex("lo"):
        # get the interface name for the index
        print(socket.if_indextoname(i))
