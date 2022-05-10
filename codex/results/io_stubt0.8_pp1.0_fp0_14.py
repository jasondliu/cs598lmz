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
print(type(view))
</code>
Using <code>RawIOBase</code> and <code>BufferedReader</code> and <code>readinto</code> (in <code>BufferedIOBase</code>) I was able to get the same results. I can assign the same type of buffer to <code>view</code> no matter what I use. Also, I can use <code>FileIO</code> the same way, without <code>BufferedReader</code>, by using <code>readinto</code>.
I thought about using <code>RawIOBase</code> for the communication, and then I can have an actual file object that is a wrapper for the <code>RawIOBase</code> object and passes any <code>read</code>/<code>write</code> calls to the <code>readinto</code>/<code>write</code> functions.

