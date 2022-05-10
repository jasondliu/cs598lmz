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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
The documentation for the <code>mmap.mmap</code> function says:
<blockquote>
<p>If length is 0, the maximum length of the map is the current size of the file when mmap is called.</p>
</blockquote>
So I would expect that I could still read the data in the file even after truncating it. Is this a bug in Python or am I doing something wrong?
I am using Python 3.6.1 on Ubuntu 16.04.


A:

The documentation is wrong. The code in <code>mmapmodule.c</code> shows that the maximum length is the size of the file when the <code>mmap</code> object is created, not when it's called.
<code>max_length = Py_MIN(filesize, PY_SSIZE_T_MAX);
</code
