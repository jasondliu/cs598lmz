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

# this should have no effect
gc.collect()

# this should raise an exception
view[0] = 0
</code>
The above code works as expected on Python 3.3.3, but not on Python 2.7.5.  In Python 2.7.5, I get the following exception:
<code>&gt;&gt;&gt; python test.py
Traceback (most recent call last):
  File "test.py", line 20, in &lt;module&gt;
    view[0] = 0
TypeError: 'str' does not support the buffer interface
</code>
Is this a bug?  If not, how should I be using <code>io.BufferedReader</code> to get the desired behavior?


A:

The documentation for <code>io.BufferedReader</code> says:
<blockquote>
<p>When a BufferedReader is created, it creates a buffer of a given size. When a block of data is read from the underlying RawIOBase, the BufferedReader adds the data to the buffer. The next read will then come from
