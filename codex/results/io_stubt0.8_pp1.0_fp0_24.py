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
Output:
<code>b''
</code>
But Python 3.8 doesn't have this problem:
<code>File("", "rb", 0)
&lt;_io.FileIO name='' mode='rb' closefd=True&gt;
File("", "r", 0)
&lt;_io.FileIO name='' mode='rb' closefd=True&gt;
File("", "wb", 0)
&lt;_io.FileIO name='' mode='wb' closefd=True&gt;
File("", "w", 0)
&lt;_io.FileIO name='' mode='wb' closefd=True&gt;
File("", "r+b", 0)
&lt;_io.FileIO name='' mode='r+b' closefd=True&gt;
File("", "r+", 0)
&lt;_io.FileIO name='' mode='r+b' closefd=True&gt;
File("", "w+b", 0)
&lt;_io.File
