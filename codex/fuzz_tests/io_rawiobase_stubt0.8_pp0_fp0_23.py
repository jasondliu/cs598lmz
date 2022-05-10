import io
class File(io.RawIOBase):
    def write(self, data):
        os.write(self.fileno(), b'\x00'*8)
        return super().write(data)

f = File()
f.write(b'Hello World!')
f.close()
</code>


A:

<blockquote>
<p>So is there a proper way to insert data before the first byte in python?</p>
</blockquote>
It depends what you mean by "proper", but there is a way that doesn't involve copying data around: use the <code>os.ftruncate</code> function before writing. 
Example
Here's my example. 
<code>import os

with open('t.dat', 'w') as f:
   f.write('hello')
</code>
Now <code>'t.dat'</code> contains <code>'hello'</code> in ASCII.
<code>with open('t.dat', 'r+b') as f:
   os.ftruncate(f.fileno(), 6)
   f.seek(0)
