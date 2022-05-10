import socket
# Test socket.if_indextoname() with a bogus

if __name__ == "__main__":
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    try:
        sock.bind(( -8L, ))
    except socket.error as ex:
        pass
    else:
        raise
