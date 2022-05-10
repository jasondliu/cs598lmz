import selectors

class HTTPResponse:
    def __init__(self, status, body):
        self.status = status
        self.body = body

class HTTPRequest:
    def __init__(self, method, path):
        self.method = method
        self.path = path
        self.headers = {}
        self.body = b''

    def add_header(self, name, value):
        self.headers[name] = value

    def add_body(self, body):
        self.body = body

class HTTPConnection:
    def __init__(self, sock, address):
        self.sock = sock
        self.address = address

        self.request = None
        self.response = None
        self.bytes_written = 0

        self.sock.setblocking(False)

        self.selector = selectors.DefaultSelector()
        self.selector.register(sock, selectors.EVENT_READ, self.on_read)
        self.selector.register(sock, selectors.EVENT_WRITE
