import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
