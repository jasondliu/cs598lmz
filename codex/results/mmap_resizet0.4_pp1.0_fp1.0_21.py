import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
With <code>f.truncate()</code> commented out, the <code>m[:]</code> line raises <code>ValueError: mmap offset is greater than file size</code>.
With <code>f.truncate()</code> uncommented, the <code>m[:]</code> line raises <code>ValueError: mmap length is greater than file size</code>.
How can I truncate a file and keep the mmap valid?


A:

<code>mmap</code> is a view into the file. If you truncate the file, the view is no longer valid.
You can use <code>mmap.resize()</code> to resize the view, but not to make it smaller.

