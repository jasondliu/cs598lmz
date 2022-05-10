import io
# Test io.RawIOBase.readall()

import support

class TestIO(io.RawIOBase):
    def readall(self):
        return b"test"

    def readable(self):
        return True

r = TestIO()

r.readall()
r.readall()
r.readall()
