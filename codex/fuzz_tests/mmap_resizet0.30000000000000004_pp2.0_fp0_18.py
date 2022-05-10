import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap closed or invalid</code>.
I understand that the mmap object is invalidated when the file is truncated, but I don't understand why I get the error when I try to access the mmap object after closing the file.
I'm using Python 3.6.5 on Linux.


A:

I think the problem is that the file is closed before the mmap object is closed.
The following code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = m[:]
</code>

