import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.encoding = encoding
        self.errors = errors
        self.newlines = newline
        self.__enter__()
        self.write(b"hello")
        self.close()
        self.__exit__()

def main():
    f = File('file.txt')
    print(f)

if __name__ == '__main__':
    main()
