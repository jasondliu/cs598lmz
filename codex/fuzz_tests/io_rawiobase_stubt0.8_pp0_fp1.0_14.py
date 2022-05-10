import io
class File(io.RawIOBase):
    def __init__(self, path, *args, **kwargs):
        super().__init__()
        self.f = io.open(path, 'rb')
    def fileno(self):
        return self.f.fileno()
    def readable(self):
        return True
    def readinto(self, b):
        return self.f.readinto(b)
    def close(self):
        return self.f.close()
    @classmethod
    def open(cls, path, *args, **kwargs):
        return cls(path, *args, **kwargs)

if __name__ == '__main__':
    print(sys.getsizeof(open('/etc/fstab', 'rb')))
    print(sys.getsizeof(File('/etc/fstab')))
</code>
Result:
<code>136
24
</code>
So, what am I missing here?


A:

I think you are misunderstanding a <code>file</code> object and a <code>RawIOBase</code>
