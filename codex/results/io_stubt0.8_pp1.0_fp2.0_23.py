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
gc.collect()
print(view[0])
</code>
You cannot use <code>io.BufferedWriter</code> because it will not accept a <code>RawIOBase</code> object as target. You could work around that by using a <code>BytesIO</code> but then you would defeat the purpose of using <code>BufferedWriter</code>.
What you could do is write your own subclass of <code>BufferedIOBase</code> that writes to memory. That way you would get all the benefits of buffering for free.

