import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.f = open(path, mode)
    def read(self, size):
        return self.f.read(size)
    def write(self, data):
        return self.f.write(data)
    def seek(self, offset, whence):
        return self.f.seek(offset, whence)
    def fileno(self):
        return self.f.fileno()
</code>
I was expecting the <code>File</code> class to behave exactly like a file object, but when I run the following code:
<code>f = File('test.txt', 'w')
print(f.read())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    print(f.read())
io.UnsupportedOperation: not readable
</code>
Why is this happening? I have implemented <code>read</code> in <code>File</code>.


A:


