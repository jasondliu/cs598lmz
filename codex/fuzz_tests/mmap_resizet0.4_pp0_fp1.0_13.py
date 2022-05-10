import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>mmap.error: cannot resize memory map</code>.
I'm not sure if this is a bug or if it's expected behavior. It seems like it would be a bug, since the docs say that <code>mmap.resize()</code> should be called when the underlying file is resized.
I'm using Python 3.6.5 on macOS 10.13.6.

