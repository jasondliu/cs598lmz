import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that the problem is that <code>f.truncate()</code> doesn't change the size of the file, but only the position of the file pointer.
Is there a way to truncate the file and keep the mmap object valid?


A:

You can use <code>mmap.resize</code> to resize the mmap object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
</code>

