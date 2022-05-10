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

gc.collect()

view.get(0)

# test __sizeof__
import sys

size = sys.getsizeof(view)
assert size >= view.sizeof() + view.itemsize * view.shape[0]

# test that only contiguous views are allowed
try:
    view = mmap[::2,1]
except ValueError:
    pass

# test __array_interface__
import struct

def get_bytes(array):
    if array.itemsize == 1:
        format = 'B'
    else:
        format = 'H'
    return struct.pack('I' + format * len(array), array.shape[0], *array)

view = mmap[::2,1]
assert view.__array_interface__ == {'data': (mmap.__array_interface__['data'][0] + 1, False),
                                    'typestr': '|u1',
                                    'shape': (mmap_size,),
                                    'strides': (2,)}
assert get_bytes(view
