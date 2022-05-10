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
del File
print(view)
</code>


A:

<blockquote>
<p>This seems to be a bug, as BufferedReader is a RawIOBase. </p>
</blockquote>
I (the original author of BufferedReader / BufferedWriter) do not consider this a bug. The behaviour is explicit, not an oversight. Objects using the buffer protocol are not required to support the <code>readinto()</code> method. 
<blockquote>
<p>this is inconsistent with the behaviour of io.BytesIO, which is also if BufferedIOBase.</p>
</blockquote>
<code>BytesIO</code> implements <code>readinto()</code>, and the documentation explicitly says that it does so. This is not inconsistent behaviour. 
<blockquote>
<p>It also prevents the use of BufferedReader with memoryview objects.</p>
</blockquote>
It does not prevent that, you just have to avoid using <code>readinto()</code> to read data into the memoryview object. You could call <code>read()</code> instead, for example.
