import socket
# Test socket.if_indextoname in C and Python

def send_ifindex():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect("\0test1")
    index = socket.if_nametoindex("lo")
    sock.sendall(str(index) + '\n')
    sock.close()

def receive_ifindex_c():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind("\0test1")
    sock.listen(50)
    newsock, addr = sock.accept()
    index = int(newsock.recv(4096))
    name = socket.if_indextoname(index)
    newsock.close()
    sock.close()
    assert name == "lo"

def receive_ifindex_python():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind("\0test1")
    sock.listen(50)
    newsock,
