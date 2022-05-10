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


A:

The default is <code>1</code>, meaning line buffering.  You need to set the buffer size using <code>io.DEFAULT_BUFFER_SIZE</code>.
<code>&gt;&gt;&gt; f = open('test.txt', 'w')
&gt;&gt;&gt; io.DEFAULT_BUFFER_SIZE = 10
&gt;&gt;&gt; f.write('hello world')
11
&gt;&gt;&gt; f.write('hello world')
11
</code>

