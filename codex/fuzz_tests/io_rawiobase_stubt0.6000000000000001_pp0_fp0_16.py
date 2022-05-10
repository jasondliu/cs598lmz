import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return b'abc'

f = File()
f.readable()

f.read(1)

f.read()

f.read()

f.read()

class File_2(io.IOBase):
    def read(self, size=-1):
        return b'abc'

f = File_2()
f.read(1)

f.read()

f.read()

f.read()

class File_3(io.BufferedIOBase):
    def read(self, size=-1):
        return b'abc'

f = File_3()
f.read(1)

f.read()

f.read()

f.read()

class File_4(io.TextIOBase):
    def read(self, size=-1):
        return 'abc'

f = File_4()
f.read(1)

f.read()

f.read()

f.read()

class File_5(io.Text
