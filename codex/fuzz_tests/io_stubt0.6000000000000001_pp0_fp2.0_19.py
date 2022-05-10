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
</code>
A few notes:

<code>io.FileIO</code> is not a file-like object, it is a stream. 
<code>io.RawIOBase</code> is a proper file-like object
<code>io.BufferedReader</code> is a wrapper over a stream that provides buffering.

If I run this with the standard CPython interpreter, I get:
<code>&gt;&gt;&gt; import io, gc, sys
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
&gt;&gt;&gt; gc.collect()
0
&gt;&gt;&gt
