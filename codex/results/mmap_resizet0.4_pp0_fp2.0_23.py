import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>b'\x01'</code>, but instead it's <code>b''</code>.
Why is that?


A:

The <code>mmap</code> object is a "view" into the file.  When you truncate the file, it's no longer the same size as the view, so the view is empty.

