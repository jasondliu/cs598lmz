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

# This should not crash.
del view

# Issue #16074: test that a BufferedReader can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a BufferedWriter can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a BufferedRWPair can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a BufferedRandom can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a TextIOWrapper can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a IncrementalNewlineDecoder can be used as a context manager.
with io.BytesIO() as f:
    pass

# Issue #16074: test that a FileIO can be used as a context manager
