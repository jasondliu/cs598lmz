import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I'm expecting to get a blank character because the file was truncated and mmap should reflect this change back. But instead I'm getting <code>Traceback (most recent call last):   File
"mmap_io.py", line 10, in &lt;module&gt;
    a = m[:]   File "/usr/lib/python3.6/mmap.py", line 369, in __getitem__
    return memoryview(self).__getitem__(idx) IndexError: index out of range</code> error. Why is that?


A:

tl;dr:
You haven't set the length of the map.  Use <code>m = mmap.mmap(f.fileno(), size=1)</code>.  Not doing so results in the map preserving its old length and not reflecting the file's truncation.

Here's the relevant bits of the implementation of what you're doing:
<code>def mmap(..., size=0, ...):
    return _mmap.mmap(...)
</code>
Data arrays are memory mapped
