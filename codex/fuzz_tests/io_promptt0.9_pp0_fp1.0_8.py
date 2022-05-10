import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readinto(self, b):
        pass
    def writable(self):
        return True
    def write(self, b):
        pass

test_pickle(RawI())
# Issue 23935: https://bugs.python.org/issue23935
import io
class MyIO(io.BytesIO):
    def __reduce_ex__(self, protocol):
        return type(self), (b'\xff',), self.__dict__

b = MyIO()
assert b.getvalue() == b'\xff'
a = pickle.loads(pickle.dumps(b))
assert a.getvalue() == b'\xff'
# Issue 23214: https://bugs.python.org/issue23214
r = io.BytesIO()
r.name = 'foobar'
r2 = pickle.loads(pickle.dumps([r]))[0]
assert r2.name == 'foobar'
# Issue 33496: https://bugs.python.org/issue33496
class
