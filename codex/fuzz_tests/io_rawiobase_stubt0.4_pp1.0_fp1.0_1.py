import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"a" * n

class C(object):
    def __init__(self):
        self.f = File()

def main():
    c = C()
    print(c.f.read(10))

main()
""")

    def test_read_error(self):
        self.assertCodeExecution("""
class File(object):
    def read(self, n=-1):
        raise Exception("read error")

class C(object):
    def __init__(self):
        self.f = File()

def main():
    c = C()
    try:
        c.f.read(10)
    except Exception as e:
        print(e)

main()
""")

    def test_readinto(self):
        self.assertCodeExecution("""
import io
class File(io.RawIOBase):
    def readinto(self, b):
        b[:] = b"a" * len(b)
        return len(b)


