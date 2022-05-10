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

global newb
newb = []
for ch in view:
    if ch in string.printable:
        newb.append(chr(ch))
    else:
       newb.append('.')
print(''.join(newb))
