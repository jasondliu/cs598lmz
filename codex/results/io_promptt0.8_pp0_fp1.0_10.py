import io
# Test io.RawIOBase subclass
import io
import sys

def test1():
    class RawIO(io.RawIOBase):
        def readall(self):
            return b"Test"

    res = str(io.StringIO(RawIO()))
    assert res == '[RawIO]', repr(res)

# Test io.TextIOBase subclass
def test2():
    class TextIO(io.TextIOBase):
        def writelines(self, lines):
            pass

    res = str(io.StringIO(TextIO()))
    assert res == '[TextIO]', repr(res)

test1()
test2()
print('passed all tests...')
