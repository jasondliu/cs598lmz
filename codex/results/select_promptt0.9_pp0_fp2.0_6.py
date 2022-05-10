import select
# Test select.select() with operable bev
import Support
support = Support.Support()

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 0))
    sock.listen(5)
    fd = sock.fileno()
    buf = array.array("B", b"X" * 1024)
    return sock, fd, buf

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", port))
    erroff = select.POLLERR | select.POLLHUP | select.POLLNVAL
    poll = select.poll()
    poll.register(sock.fileno(), select.POLLIN | erroff)
    sock.close()
    support.eventually(lambda : poll
