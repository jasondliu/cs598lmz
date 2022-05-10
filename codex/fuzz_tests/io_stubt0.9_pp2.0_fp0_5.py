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
"""
#
#  readinto test with array.array
#
from io import BytesIO
import array
s = b'1'
f = BytesIO(s)
view = array.array('b', [0])
f.readinto(view)
"""
#
#  readline test with BufferedReader
#
from io import BytesIO
f = BytesIO(b'abc')
b = f.readline()
"""
#
#  readline test with BytesIO
#
from io import BytesIO
f = BytesIO(b'abc')
b = f.readline()
"""
#
#  readline test with StringIO
#
from io import StringIO
f = StringIO('abc')
b = f.readline()
"""
#
#  readlines test with BufferedReader
#
from io import StringIO
f = StringIO('1\n2\n3')
a = f.readlines()
"""
#
#  readlines test with StringIO
#
from io import StringIO
f
