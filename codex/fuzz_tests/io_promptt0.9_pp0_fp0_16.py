import io
# Test io.RawIOBase subclass
class net_io(io.RawIOBase):

    def read(self, n=-1):
        if n == -1:
            n = 10
        return b'0'*n

    def readable(self):
        return True

    def writable(self):
        return True

    def write(self, b):
        if len(b) > 3:
            return -1
        else:
            return len(b)

#Test io.BufferedIOBase subclass
class net_bi(io.BufferedIOBase):

    def read(self, n=-1):
        if n == -1:
            n = 10
        return b'0'*n

    def readable(self):
        return True

    def writable(self):
        return True

    def write(self, b):
        if len(b) > 3:
            return -1
        else:
            return len(b)

    def flush(self):
        pass

#Test io.TextIOBase subclass
class net_ti(io.TextIOBase):

    def read
