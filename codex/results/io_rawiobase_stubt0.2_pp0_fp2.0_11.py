import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = io.open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

def open(filename, mode):
    return File(filename, mode)

def main():
    with open('/etc/passwd', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    main()
