import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file 
    def readable(self):
        return True 
    def readinto(self, b):
        v = self.file.read(len(b))
        n = len(b)
        try:
            b[:len(v)] = v
        except TypeError as err:
            raise TypeError("readinto() argument 1 must be a writable buffer, not %s" % type(b).__name__)
        return n
 
class Socket(io.RawIOBase):
    def __init__(self, socket):
        self.socket = socket

    def readable(self):
        return True 

    def readinto(self, b):
        l = len(b)
        v = self.socket.recv(l)
        n = len(v)
        try:
            b[:n] = v
        except TypeError as err:
            raise TypeError("readinto() argument 1 must be a writable buffer, not %s" % type(b).__name__)
       
