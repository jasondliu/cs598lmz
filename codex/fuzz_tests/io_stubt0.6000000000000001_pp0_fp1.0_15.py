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
</code>
This gives me the expected result:
<code>&gt;&gt;&gt; view
bytearray(b'\x00')
</code>
However, I cannot find a way to make an equivalent class that inherits from <code>io.TextIOBase</code>.


A:

You can use the <code>TextIOBase.readinto</code> method, which is documented as:
<blockquote>
<p>Read up to <em>n</em> characters into <em>buffer</em> and return the number of characters read. If the underlying raw stream is not in a codepoint boundary, the method will stop at the boundary and return the number of characters read. If <em>n</em> is negative or omitted, read until EOF using multiple read() calls.</p>
</blockquote>
If you want to read a single byte, you can use <code>n=1</code>:
<code>&gt;&gt;&gt; class File(io.TextIOBase):
...     def readinto(self, buf):
...         global view

