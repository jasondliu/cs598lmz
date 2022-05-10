import io
class File(io.RawIOBase):
    def read(self, n=-1):
        '''Read and return at most n bytes.
        Implemented entirely *in Python* on top of readinto();
        core code from <code>io.py</code>'''
        if n is None:
            n = -1
        elif not isinstance(n, int_types):
            raise TypeError("an integer is required")
        if n < 0:
            return self.readall()
        b = io.BytesIO()
        while 1:
            if not hasattr(self, '_readinto'):
                buffer = self.read(n - len(b))
            else:
                buffer = bytearray(n - len(b))
                nbytes = self._readinto(buffer)
                if nbytes == 0:
                    break
                buffer = bytes(buffer[:nbytes])
            if not buffer:
                break
            n -= len(buffer)
            b.write(buffer)
            if 0 < n <= len(buffer):
                b.seek(-n, 1)
                b = b
