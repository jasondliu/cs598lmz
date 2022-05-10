import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def read(self):
        return 'read'
# f = File()
# f.
import io
# class File(io.RawIOBase):
# class File(io.BufferedIOBase):
class File(io.TextIOBase):
    def __init__(self):
        pass
    def read(self):
        return 'read'

f = File()

len(f.read())

len(f.read())

f.read() == ''

len(f.read())

f
f.closed
f.close()
f.closed
import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def read(self):
        return 'read'
f = File()
f.read()

f.read()

f.read()

f.read()

f.read()

import io
class File(io.RawIOBase):
    def __init__(self):
        self.buf = ''
    def read
