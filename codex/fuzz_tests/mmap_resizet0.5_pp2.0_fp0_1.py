import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
returns
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 6, in &lt;module&gt;
ValueError: mmap closed or invalid
</code>


A:

<code>mmap</code> will be invalidated by <code>truncate</code> and <code>close</code>, but not by <code>flush</code>.
<code>mmap</code> will also be invalidated if you <code>open</code> the file in a different mode.
<code>mmap</code> is no longer invalidated by <code>flush</code> in Python 3.3.

