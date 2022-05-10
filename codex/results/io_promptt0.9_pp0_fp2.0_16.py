import io
# Test io.RawIOBase
# r)ead
# w)rite
# a)ppend
# b)inary
# s)tring

class wbprinter(io.RawIOBase):
    def write(self,b):
        print("Got {} bytes".format(len(b)))
        for b in b:
            print("{}".format(b))
        return len(b)

class wbrecorder(io.RawIOBase):
    def read(self,b):
        pass

    def write(self,b):
        print("Got {} bytes".format(len(b)))
        self.buf = b

class wbreaderer(io.RawIOBase):
    def __init__(self,s):
        self.s = s
    def read(self,b):
        ret = self.s[0:b]
        self.s = self.s[b:]
        return ret
    def seekable(self):
        print("This one is seekable!")
        return True

rec = wbrecorder()
w = io.BufferedWriter(
