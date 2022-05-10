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
It prints <code>None</code> when I run it with Python 3.5.0, but prints <code>b'\x00'</code> when I run it with Python 3.4.3. 
I'm working on a library that needs to work with Python 3.4 as well as 3.5 and above, and I'm wondering if I'm misusing <code>io</code> and this was just a bug in 3.4 that got fixed in 3.5, or if it changed on purpose and there's a better way to do what I want.  I want to be able to write an object that can both create a <code>BufferedReader</code> and also read in data into the <code>BufferedReader</code>'s buffer.  I'm aware that in Python 3.4 and above, <code>io.BufferedReader</code> is a subclass of <code>io.RawIOBase</code> and could be used directly, but I want it to work with lower versions of Python as well.

