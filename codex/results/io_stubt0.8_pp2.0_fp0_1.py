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
print(len(view))
</code>
This outputs 1 on Python 2 and 0 on Python 3.3 and 3.4. On Python 3.5, it outputs <code>TypeError: weakly-referenced object no longer exists</code> for a different reason.
Python 3.2 is no longer supported, and 3.5 is still in development, so if you want to support both, you'll have to maintain compatibility. I think the approach I described in the previous paragraph would be the best option.

