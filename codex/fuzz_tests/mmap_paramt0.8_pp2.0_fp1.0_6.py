import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "mmap.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
TypeError: mmap: need valid fileno.
</code>
I am running this on Windows 7 with Python 3.4.
What's wrong?


A:

According to the documentation, the size parameter must be positive and not zero.
<blockquote>
<p>The size argument specifies the size in bytes of the buffer used to represent the memorymap. It must be 0. </p>
</blockquote>
Moreover, the Windows version of Python does not support mapping of empty files.
From the Python 3.5 source code:
<code>static PyObject *
mmap_new(PyTypeObject *type, PyObject *args, PyObject *kwdict)
{
    ...
    const char *tagstr;
    int flags = MAP_SHARED;
    int prot = PROT_WRITE |
