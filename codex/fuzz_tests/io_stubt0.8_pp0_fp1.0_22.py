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
</code>
This generates the following error:
<code>Exception ignored in: '_io.BufferedIOBase.__del__'
Traceback (most recent call last):
  File "C:\Python35\lib\io.py", line 851, in __del__
  File "C:\Python35\lib\io.py", line 718, in close
  File "C:\Python35\lib\io.py", line 528, in close
  File "C:\Users\Tester\AppData\Local\Temp\tmp4z4k4fmi\test.py", line 9, in close
  File "C:\Python35\lib\gc.py", line 111, in collect
TypeError: cannot create weak reference to 'bytearray' object
</code>
The error occurs because <code>BufferedReader</code> has a list of <code>bytearray</code> objects in its <code>buffer</code> attribute; this list is weakly referenced so that it can be garbage collected when <code>BufferedReader</code> is no longer in
