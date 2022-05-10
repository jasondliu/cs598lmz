import io
# Test io.RawIOBase which calls readline
class TSR(io.RawIOBase):
    def readline(self):
        return 'Foo'
