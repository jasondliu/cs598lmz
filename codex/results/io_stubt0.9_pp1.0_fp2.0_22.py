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

f = io.BufferedRandom(File())
f.close()

#print(len(view))
assert view is None or len(view) == 1

#===[Backwards compatibility tests]=======================================
f = io.BytesIO(b"a" * 10)
m = memoryview(f.getbuffer());
assert m.format == "B"
m = m[::-1]
assert m.format == "B"
assert m.tobytes() == b"aaaaaaaaaa"

f = io.BytesIO()
m = memoryview(f.getbuffer());
assert m.format == "B"

f = io.StringIO()
#f.getbuffer()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: underlying buffer is not writable

f = io.BytesIO(b"abc")
m = memoryview(f).cast("h")
assert m.format == "h"
m.release()

f = io.BytesIO(b"a" *
