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

#import array
#view = array.array('B', view)

#print(len(view))

#print(view)

#print(view[0x2b])
#print(view[0x2c])
#print(view[0x2d])
#print(view[0x2e])
#print(view[0x2f])
#print(view[0x30])
#print(view[0x31])
#print(view[0x32])
#print(view[0x33])
#print(view[0x34])
#print(view[0x35])
#print(view[0x36])
#print(view[0x37])
#print(view[0x38])
#print(view[0x39])
#print(view[0x3a])
#print(view[0x3b])
#print(view[0x3c])
#print(view[0x3d])
#print(view[0x3e])
#print(view[0x
