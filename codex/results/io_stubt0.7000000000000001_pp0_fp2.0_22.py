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

print(memoryview(view).tobytes())
</code>
Error:
<code>Traceback (most recent call last):
  File "C:/Users/nicholas/AppData/Local/Programs/Python/Python38-32/Test/test.py", line 13, in &lt;module&gt;
    print(memoryview(view).tobytes())
ValueError: memoryview: underlying buffer is not C contiguous
</code>
Printing the memoryview shows that it is just the one byte, but the bytes itself return an empty byte string.

