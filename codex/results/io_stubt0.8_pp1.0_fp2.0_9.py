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
print(view)
</code>
I wanted to do
<code>f.readinto(buf)
del f
</code>
but it seems that it is not possible. Is there any reason why readinto cannot be used that way? 


A:

<code>readinto</code> mutates the object it's called on, and it's not possible to know how many bytes were actually read, so there are various kinds of buffering that are not possible without making a mess.
That's why we have <code>read</code> and <code>readinto</code> - the former is for streams where you know you can skip arbitrary bytes, the latter for streams that are always readable and where you can't skip ahead.

