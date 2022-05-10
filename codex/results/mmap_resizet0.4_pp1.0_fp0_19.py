import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And I get the error <code>ValueError: mmap can't resize a readonly or copy-on-write memory map</code>.
How can I get the contents of the file after truncating it?


A:

You can't.  The <code>mmap</code> object is a view into the file, and when you truncate it, the view is no longer valid.

