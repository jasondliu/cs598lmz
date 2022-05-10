import select
# Test select.select
def make_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(('localhost', 0))
    sock.listen(5)
    return sock

def make_connected_socket():
    sock = make_socket()
    port = sock.getsockname()[1]

    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect(('localhost', port))
    return sock, csock

def test_select():
    sock, csock = make_connected_socket()

    sock.close()
    csock.close()

# Test select.poll
def test_poll():
    sock, csock = make_connected_socket()
    poll = select.poll()
    poll.register(sock, select.POLLIN)
    poll.poll()
