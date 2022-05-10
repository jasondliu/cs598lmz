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
print(view)
</code>
This does not work on Python 3.8, but does work on Python 3.7 and earlier.
The error message is:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    print(view)
TypeError: 'NoneType' object is not callable
</code>
The problem is that the <code>PyObject_GC_UnTrack</code> call in <code>PyBuffer_Release</code> tries to call a function whose address is <code>0x0</code>. This causes the crash.
On Python 3.7 and earlier, this address is not <code>0x0</code>. On Python 3.8, it is <code>0x0</code>.
How do I fix this? I have tried to use <code>gc.disable()</code>, but that does not work.

