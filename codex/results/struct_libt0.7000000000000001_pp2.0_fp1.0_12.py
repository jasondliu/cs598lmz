import _struct
import _thread

# todo: credentials

class Client(object):
    def __init__(self, address, port, user, password, cert=None, verify=True, ca_cert=None, timeout=5):
        self.address = address
        self.port = port
        self.user = user
        self.password = password
        self.cert = cert
        self.verify = verify
        self.ca_cert = ca_cert
        self.timeout = timeout
        self.conn = None
        self.last_command = 0
        self.connect()

    def connect(self):
        if self.conn:
            self.conn.close()

        self.conn = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        self.conn.connect((self.address, self.port))
        self.conn.settimeout(self.timeout)

    def disconnect(self):
        self.conn.close()

    def send(self, *args):
        self.conn.send(_struct.pack('<i', len
