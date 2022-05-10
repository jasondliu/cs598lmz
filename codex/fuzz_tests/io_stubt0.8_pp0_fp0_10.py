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
print(len(view))
</code>
On my python 3.4 it prints <code>1</code> but the printed value changes when I look at it in the debugger. 
And if I call <code>gc.collect()</code> a second time it prints <code>0</code>.

