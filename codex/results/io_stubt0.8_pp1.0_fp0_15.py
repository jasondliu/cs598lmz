import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f  # Help out the garbage collector
print(view)  # Won't be freed until f is deleted
</code>
It's possible to get an actual reference that can be kept and won't be freed, but I don't think it would be worth the effort. I'll just note that the <code>buffer</code> object that <code>memoryview</code> is based on has a <code>release</code> method.

