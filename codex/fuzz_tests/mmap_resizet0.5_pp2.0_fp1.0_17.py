import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I tested this on Windows and Linux. The same code works on Linux with Python 3.6.
Is this a bug in Python 3.7 or am I doing something wrong?


A:

I'm not sure if this is a bug in Python 3.7, but I found a solution that works on Windows and Linux.
The problem is that <code>mmap</code> keeps the file size in memory and doesn't update it when the file is truncated. It only updates it when the file is closed.
So the solution is to close the <code>mmap</code> object before truncating the file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(
