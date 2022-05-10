import io
class File(io.RawIOBase):
    def __init__(self, s):
        self.s = s
        self.fd = s.fileno()
        self.seek(0)
    def readable(self):
        return True
    def readinto(self, b):
        return self.s.recv_into(b)
    def read(self, l):
        return self.s.recv(l)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.s.setblocking(False)
            while True:
                try:
                    self.s.recv(offset, socket.MSG_PEEK)
                    return
                except BlockingIOError:
                    pass
        elif whence == 2:
            raise NotImplementedError
        else:
            raise ValueError
    def tell(self):
        raise NotImplementedError
    def writable(self):
        return False
</code>
I have skipped a lot of checks and error handling. This code is just an example, not to be
