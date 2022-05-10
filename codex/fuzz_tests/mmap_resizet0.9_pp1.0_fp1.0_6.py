import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

os.remove('test')
</code>
I get an exception:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 4, in &lt;module&gt;
ValueError: mmap length is zero
</code>
But with <code>m.resize(1)</code> instead of <code>f.truncate()</code> this doesn't happen.
Why is this? Shouldn't they both extend the underlying file, thus the length of the mmap should become non-zero?


A:

<code>.truncate()</code> operation alters the file size (see <code>os.truncate</code> manual) and the memory mapped area is indeed empty:
<code>import os
import mmap

with open('test', 'wb') as f: 
    f.write(bytes(1))

with open('test', 'r+b') as f: 
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
