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
print bytes(view)
</code>
This yields the error
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    print bytes(view)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 0: ordinal not in range(128)
</code>
The memoryview is filled with bytes containing 0xff and the line <code>print bytes(view)</code> throws the error. This does not happen when the print command is removed.
I am using Python 3.3 on Windows 7, if that matters.
My question is, why does the print command cause an error and what is the correct way to print the memoryview of bytes?
Many thanks!


A:

In python 3, the <code>bytes()</code> function returns an immutable bytes object, which is just like a string in terms of its underlying representation (i.e. the <code>__bytes__</code> method returns <code>self</code>), but the <code>repr()</code> of it is different.
