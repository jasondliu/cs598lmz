import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
This code works fine on OSX, but on Linux it throws an exception:
<code>  File "/usr/lib/python3.4/mmap.py", line 279, in __setitem__
    raise TypeError('Cannot modify read-only memory')
TypeError: Cannot modify read-only memory
</code>
Is there any way to write to the file without closing the mmap object?

