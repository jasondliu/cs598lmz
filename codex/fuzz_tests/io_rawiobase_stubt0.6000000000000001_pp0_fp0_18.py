import io
class File(io.RawIOBase):
    def __init__(self):
        self.buffer = io.BytesIO()
        self.mode = "wb"
    def write(self, s):
        self.buffer.write(s)
    def seek(self, offset, whence=0):
        self.buffer.seek(offset, whence)
    def read(self, n=-1):
        return self.buffer.read(n)
    def tell(self):
        return self.buffer.tell()
    def flush(self):
        pass
    def close(self):
        self.buffer.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.buffer.close()

def main():
    out = File()
    out.write(b"Hello World\n")
    out.seek(0)
    print(out.read())
    out.close()

if __name__ == "__main__":
    main()
