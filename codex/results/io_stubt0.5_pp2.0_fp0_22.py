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
<code>&gt;&gt;&gt; import io
&gt;&gt;&gt; 
&gt;&gt;&gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = buf
...     def readable(self):
...         return True
... 
&gt;&gt;&gt; f = io.BufferedReader(File())
&gt;&gt;&gt; f.read(1)
b''
&gt;&gt;&gt; del f
&gt;&gt;&gt; print(view)
None
</code>

