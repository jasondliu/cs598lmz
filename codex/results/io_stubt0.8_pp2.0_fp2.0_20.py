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

buf = view
del view

print(buf)

# test that the buffer attributes are still what they should be.
import array
a = array.array('B', 'a'*10)

import ctypes
buf = ctypes.create_string_buffer(1)
print('buf[0] = ' + repr(buf[0]))

buf[0] = 'a'
print('buf[0] = ' + repr(buf[0]))

buf[0] = '\u1234'
print('buf[0] = ' + repr(buf[0]))

buf[0] = 0xff
print('buf[0] = ' + repr(buf[0]))

buf[0] = 0x100
print('buf[0] = ' + repr(buf[0]))

buf[0] = -1
print('buf[0] = ' + repr(buf[0]))

buf[0] = -256
print('buf[0] = ' + repr(buf[0]))

buf[0] = a[0
