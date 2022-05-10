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
sys.getrefcount(view)
# 64
(memoryview(view) is view)
# True

f = File()
f.readinto(view)
del f
sys.getrefcount(view)
# 2
(memoryview(view) is view)
# True
</code>
with python 3.6.1 it is even worse:
<code>import sys
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
sys.getrefcount(view)
# 2
(memoryview(view) is view)
# False     &lt;--------

f = File()
f.readinto(view)
del f
sys.getrefcount(view)
# 1
(memoryview(view) is view)
# False     &lt;--------
</code>
This means that <code>readinto</code> is no longer guaranteed to return
