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
Demonstrated on the REPL:
<code>&gt;&gt;&gt; import io
&gt;&gt;&gt; view = None
&gt;&gt;&gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = buf
...     def readable(self):
...         return True
...
&gt;&gt;&gt; f = io.BufferedReader(File())
&gt;&gt;&gt; f.read(1)
b'\x00'
&gt;&gt;&gt; del f
&gt;&gt;&gt; print(view)
None
</code>
Now, for the <code>BufferedReader</code> class, I have to assume that the <code>readinto</code> method is defined and implemented as something similar to:
<code>def readinto(self, buf):
    return self.raw.readinto(buf)
</code>
I assume that the <code>BufferedReader
