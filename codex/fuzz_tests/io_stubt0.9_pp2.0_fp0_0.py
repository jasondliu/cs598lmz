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

print('{:08b}'.format(view[0]))
</code>
I expect to see 1010 1010. but instead, I see the exception:
<code>TypeError: 'BufferedReader' does not support the buffer interface
</code>
Is there any way I can mutate a slice of <code>bytes</code> in this way?


A:

I think the problem is that you're opening a <code>io.BufferedReader</code> on the raw <code>File</code> object rather than a <code>io.FileIO</code> object, and the two types of objects aren't interchangeable. <code>io.BufferedReader</code> is the underlying object created by <code>io.open</code>, but it can't do arbitrary file operations like memory mapping.
If you want to read data from a <code>File</code> object, you should probably open a <code>io.FileIO</code> instead. I just tried it:
<code>import array
import io

class File(io.RawIOBase):
    filename = "example.txt"

