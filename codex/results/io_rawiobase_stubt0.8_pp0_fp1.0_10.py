import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.buf = ""
        self.bapp = 0
        self.fapp = 0

    def fileno(self):
        return self.f.fileno()

    def readinto(self, b):
        while True:
            bb = self.buf[self.bapp:len(self.buf)]
            if len(bb) == 0:
                return 0
            if len(bb) > len(b):
                bb = bb[0:len(b)]
            b[0:len(bb)] = bb
            self.bapp += len(bb)
            return len(bb)

    def write(self, b):
        self.f.write(b)
        self.f.flush()
        self.fapp += len(b)
        return len(b)

class MySocket(object):
    def __init__(self, sock, handshake=False):
        self.sock = sock

    def sendall(self, data):
        self.fil
