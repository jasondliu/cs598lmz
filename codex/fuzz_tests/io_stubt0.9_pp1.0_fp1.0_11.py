import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

assert len(view) == buf_len

def cb():
    buf = memoryview(b"\0" * buf_len)
    assert len(buf) == buf_len
    return buf

def f(n):
    def g(m, p0, p1, p2, p3, p4, p5, p6):
        return m
    return g

# a simplified version of the case in #17773
def f_call():
    for i in range(20):
        f(i)()

f_call()
# it has to also work on the JIT-trace
f(20)

from _testcapi import formattest
assert formattest(b' ') == b"b' '"
assert formattest(b'\0') == b"b'\\x00'"

# and we also have to reach this line in the JIT-trace
from _testcapi import formattest
formattest(b' ') != b"b' '"
formattest(b'\0') != b"
