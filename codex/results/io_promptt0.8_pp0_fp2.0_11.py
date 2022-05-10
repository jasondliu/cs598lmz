import io
# Test io.RawIOBase
class C(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0

C()

# Test io.BufferedIOBase
class D(io.BufferedIOBase):
    def readinto(self, b):
        return 0

D()
# Test io.TextIOBase
class E(io.TextIOBase):
    @property
    def encoding(self):
        return "ascii"
    @property
    def errors(self):
        return "replace"
    @property
    def newlines(self):
        return None
    def readinto(self, b):
        return 0

E()

# Test io.RawIOBase
class F(io.RawIOBase):
    def readable(self):
        return True
    def buffered(self):
        return C()
    def readinto(self, b):
        return 0

F()
