import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    
    def read(self, n=-1):
        return self.fd.read(n)
    
    def write(self, b):
        return self.fd.write(b)
    
    def readable(self):
        return True
    
    def writable(self):
        return True
    
    def seekable(self):
        return True
    
    def seek(self, n, origin=0):
        return self.fd.seek(n, origin)
    
    def close(self):
        return self.fd.close()
    
    def fileno(self):
        return self.fd.fileno()


class Socket(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    
    def readinto(self, buffer):
        return self.fd.recv_into(buffer)
    
    def write(self, bytes):
        return self.fd.send(bytes)
    
   
