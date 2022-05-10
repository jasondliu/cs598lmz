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
view # unresolved; stays the same between experiments
 
# Variables are correctly contained in the instance
#
# EXPECTED OUTPUT:
#
# <class '__main__.File'>
# False
# 8: <class 'memoryview'>
# 6: <class 'memoryview'>
# """
