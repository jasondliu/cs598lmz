import io
class File(io.RawIOBase):
    def readable(self):
        pass

    def readinto(self):
        pass

    def read(self):
        pass

    def seekable(self):
        pass

    def seek(self, pos, whence=0):
        pass

    def tell(self):
        pass

    def writeable(self):
        pass

    def writelines(self, lines):
        pass

    def write(self, b):
        pass

    def read1(self, n=-1):
        pass

def TextIOWrapper(file, encoding, errors='strict', newline=None, line_buffering=False):
    pass

def IOBase(buf):
    pass

def BufferedIOBase(raw, buffer_size=DEFAULT_BUFFER_SIZE):
    pass

def BytesIO(initial_bytes=None):
    pass

def StringIO():
    pass

# Workaround for https://github.com/yokawasa/pyimmutable/issues/16
# We need to make sure that this is not added to the global namespace.

