import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b"foo"

RawI().read()
# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def read(self, n=-1):
        return b"foo"

BufferedI().read()
# Test io.TextIOBase
class TextI(io.TextIOBase):
    def read(self, n=-1):
        return "foo"

TextI().read()
# Test io.BytesIO
io.BytesIO(b"foo").read()
# Test io.StringIO
io.StringIO("foo").read()
# Test io.BufferedReader
io.BufferedReader(io.BytesIO(b"foo")).read()
# Test io.BufferedWriter
io.BufferedWriter(io.BytesIO()).write(b"foo")
# Test io.BufferedRWPair
io.BufferedRWPair(io.BytesIO(), io.BytesIO()).read()
# Test io.Buff
