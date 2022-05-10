import io
class File(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def read(self, n=-1):
        res = self.data[self.pos : self.pos + n]
        self.pos += n
        return res

class Transaction:
    dbs = {
        'default': 1,
        'index': 2,
    }

    def __init__(self, db, host='localhost', port=4747, credential=None):
        self.db = db
        self.host = host
        self.port = port
        self.credential = credential
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.sockfile = File(self.sock.makefile())
        self.version = self.sockfile.read(7).decode('utf-8')
        self.sock.sendall(b'\x03')
        data = self.sockfile.read(1)
        if data != b'\x00':
            raise
