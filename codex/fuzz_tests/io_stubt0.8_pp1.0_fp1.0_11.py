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

bytes(view)
</code>
This throws:
<code>TypeError: a bytes-like object is required, not 'memoryview'
</code>
So I'm left wondering: if <code>memoryview.cast()</code> performs such a conversion, is it also possible to perform such a conversion without using <code>memoryview</code>? 
Or does it simply happen to be the case that <code>memoryview.cast()</code> performs a conversion but that it is not actually possible to perform such a conversion elsewhere?
Note: I'm aware of <code>bytes(memoryview(buf))</code>. This is not what I'm looking for, since it's not possible to write a <code>File</code> subclass which returns a <code>memoryview()</code>.


A:

It's explicitly documented that <code>memoryview.cast</code> creates a new object, so you can't access it directly using <code>memoryview</code>:
<code>&gt;&gt;&gt; c = memoryview(b'abc')
&gt;&gt;&gt; c

