import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def close(self):
        self.file.close()

def _get_file_handle(file, mode, encoding, errors):
    if isinstance(file, str):
        return open(file, mode, encoding=encoding, errors=errors)
    elif hasattr(file, "read") or hasattr(file, "write"):
        return file
    else:
        raise ValueError("Invalid file: %r" % file)

def _validate_mode(mode):
    if not isinstance(mode, str):
        raise TypeError("invalid file mode: %r" % mode)

    if mode not in ("r", "w", "x", "a", "r+", "w+", "x+", "a+", "rb", "wb", "xb", "ab
