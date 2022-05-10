import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The first time I run the script, the output is:
<code>b'\x01'
b''
</code>
The second time I run the script, the output is:
<code>b'\x01'
Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure what the behavior is supposed to be, but it seems like the mmap is not being updated when the underlying file is truncated.  Is this a bug?  Am I doing something wrong?
I'm using Python 3.6.4 on Ubuntu 16.04.


A:

This is a known issue with <code>mmap</code> on Linux.  See https://bugs.python
