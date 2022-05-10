import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows and Linux, but on Mac OS X it results in a <code>ValueError</code> exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
It's a bit strange, because the file size is 0 and the offset is 0, so the offset should be less than the file size.
I've tried to find the reason for this behavior in the mmap source code, but I haven't found anything.
Is there any way to make this code work on Mac OS X?


A:

I've found a solution:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
