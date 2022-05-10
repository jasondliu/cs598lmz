import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.file = file

    def readable(self):
        return True

    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        b[:n] = data
        return n

with File(open('data.bin', 'rb')) as f:
    print(f.read())
</code>


A:

Your implementation is almost right. The only difference is that you need to override <code>read</code> instead of <code>readinto</code>:
<code>class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.file = file

    def readable(self):
        return True

    def read(self, n=-1):
        return self.file.read(n)
