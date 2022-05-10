import io
# Test io.RawIOBase
class test(io.RawIOBase):
    def write(self, s):
        print("RawIOBase.write called: %s"%s)

    def flush(self):
        print("RawIOBase.flush called")

t = test()
t.write(b'123')
t.flush()

# Test io.BufferedIOBase
class test2(io.BufferedIOBase):
    def write(self, s):
        print("BufferedIOBase.write called: %s"%s)

    def flush(self):
        print("BufferedIOBase.flush called")

t2 = test2()
t2.write(b'123')
t2.flush()
