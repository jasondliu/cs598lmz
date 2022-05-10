import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
But when I run this, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: write() argument 1 must be str, not bytes
</code>
I am using Python 2.7.10 on Ubuntu 16.04. I found this question, and tried using <code>m.write(bytes(2))</code>, but that doesn't work either.


A:

It seems you're using the wrong <code>bytes</code> constructor.
The <code>bytes</code> constructor you're using is equivalent to Python 3's <code>bytes()</code>, which creates an immutable array of bytes.
The <code>bytes</code> constructor you want is equivalent to Python 3's <code>bytearray()</code>, which creates a mutable array of bytes.
The Python 2 <code>bytes</code> constructor is deprecated, and the documentation suggests you use <code>by
