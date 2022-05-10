import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Expected output:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap can't extend file
</code>
Actual output:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
TypeError: a bytes-like object is required, not 'mmap.mmap'
</code>
Is this a bug in Python 3.4.0?
If so, how do I work around it?


A:

This is a bug in Python 3.4.0.

