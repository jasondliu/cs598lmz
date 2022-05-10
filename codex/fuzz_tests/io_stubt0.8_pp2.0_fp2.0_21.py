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
del view
</code>
Result:
<code>$ python2.7-dbg -m pdb test.py 
&gt; /tmp/test.py(14)&lt;module&gt;()
-&gt; f = io.BufferedReader(File())
(Pdb) print view
&lt;memory buffer at remote 0x7fffbfe5cc08&gt;
</code>
With a little help from this SO answer I was able to isolate the relevant part of the code and make it work with 3.2 as well:
<code>import ctypes
from ctypes import pythonapi, c_void_p, c_ssize_t

pythonapi.PyBuffer_Release.argtypes = [c_void_p]

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)

# release memoryview to allow GC to collect it
pythonapi.PyBuffer_Release
