import io
class File(io.RawIOBase):
    """Dummy class to have the same interface as in ftplib.py."""
    def close(self):
        pass

class FTP:
    debugging = 0
    host = '127.0.0.1'
    port = 21
    maxline = 8192
    welcome = '220 ready.'
    file = None
    sock = None
    passive = True
    af = socket.AF_INET
    ap = socket.IPPROTO_TCP

    def __init__(self, host='', port=0, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.timeout = timeout
        if host:
            self.connect(host, port)

    def connect(self, host='', port=0):
        if not port:
            i = string.find(host, ':')
            if i >= 0:
                host, port = host[:i], host[i + 1:]
                try:
                    port = int(port)
                except ValueError:
                    raise socket.error, "nonnumeric port"
        if not port:
