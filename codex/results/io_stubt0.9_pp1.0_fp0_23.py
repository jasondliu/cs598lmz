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

## body partstart: string
print(view)
## body partend

## body partstart: bytes
print(repr(view))
## body partend
