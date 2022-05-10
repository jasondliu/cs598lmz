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
This is just a hack, but it works:
<code>&gt;&gt;&gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = bytearray(buf)
...     def readable(self):
...         return True
... 
&gt;&gt;&gt; f = io.BufferedReader(File())
&gt;&gt;&gt; f.read(1)
b'\x00'
&gt;&gt;&gt; view
bytearray(b'\x00')
&gt;&gt;&gt; 
</code>

