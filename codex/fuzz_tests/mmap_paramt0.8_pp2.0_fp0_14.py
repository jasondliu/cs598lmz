import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0, 0)
    m[0:5] = bytes('12345', 'utf-8')
</code>
And I have the following error: 
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0:5] = bytes('12345', 'utf-8')
TypeError: slice indices must be integers or None or have an __index__ method
</code>
I'm referring to this doc: https://docs.python.org/3/library/mmap.html


A:

You must pass integers as indices, not slice objects, to the <code>__setitem__</code> method, just as you would with a standard Python list.
<code>m[0:5] = bytes('12345', 'utf-8')
</code>
should be
<code>m[0:5] = bytes('12345', 'utf-8')
</code>

