import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"foo"

f = File()
f.read()

# $ python3 io_raw.py
# b'foo'

# $ python2 io_raw.py
# Traceback (most recent call last):
#   File "io_raw.py", line 8, in <module>
#     f.read()
# TypeError: read() takes exactly 1 argument (0 given)
