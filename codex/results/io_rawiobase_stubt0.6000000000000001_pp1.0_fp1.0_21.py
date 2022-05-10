import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"\0" * n
    def write(self, b):
        return len(b)
f = File()
f.read(10)

f.write(b"hello world")

f.fileno()

f.isatty()

f.tell()

f.seek(3)

f.seek(3, 1)

f.seekable()

f.readable()

f.writable()

f.readline()

f.readlines()

f.write(b"this is a test\n")

f.writelines([b"first\n", b"second\n"])

f.seek(0)

f.truncate()

f.flush()

f.close()

import io
content = b"this is the content"
f = io.BytesIO(content)
f.read()

with io.BytesIO(content) as f:
    print(f.read())

import io
content = b"this
