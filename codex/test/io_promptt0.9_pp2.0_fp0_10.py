import io
# Test io.RawIOBase.
# NOTE: io.RawIOBase.readline seems to have a bug, so we have our own RawIO mock
class RawReadMock(io.RawIOBase):
    def __init__(self, s):
        self.s = s
        self.pos = 0
    def readline(self, index=None):
        if index is None:
            index = len(self.s)
        t = self.s[self.pos:index]
        self.pos = index
        return t
    def readlines(self, numlines=None):
        ans = []
        if numlines is None:
            numlines = len(self.s)
        for i in range(numlines):
            line = self.readline()
            if line == "":
                break
            ans.append(line)
        return ans
    def tell(self):
        return self.pos
    def close(self):
        pass
s = "A\nB\nC\n"
tt = RawReadMock(s)
