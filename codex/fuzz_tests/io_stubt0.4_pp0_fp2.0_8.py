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
view[0] = 0
</code>
As you can see, the <code>File</code> class is a simple implementation of the <code>RawIOBase</code> interface. The <code>readinto</code> method simply receives a buffer and stores it in a global variable (which is bad, I know, but it's just an example).
When I run the code, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    view[0] = 0
TypeError: 'NoneType' object does not support item assignment
</code>
I was expecting the <code>view</code> variable to be a <code>bytearray</code> object, but it's <code>None</code>.
What am I doing wrong?


A:

The <code>io</code> module is meant to be used with file-like objects that implement the <code>RawIOBase</code> interface. It's not meant to be used with objects that implement only a subset of that interface, such as <
