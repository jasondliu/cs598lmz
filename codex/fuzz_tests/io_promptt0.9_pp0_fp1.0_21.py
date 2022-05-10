import io
# Test io.RawIOBase.readinto(), the pure C function _PyObject_CallMethodId()

class Calling(io.RawIOBase):
    def readinto(self, l):
        l[:2] = [ord(s) for s in "ab"]
        l[2:4] = [ord(s) for s in "cd"]
        return len(l)

    def readable(self):
        return True

with support.captured_stdout() as p:
    print(Calling().read(10))
