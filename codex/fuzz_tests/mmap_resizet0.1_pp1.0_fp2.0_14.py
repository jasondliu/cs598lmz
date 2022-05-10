import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that the problem is that <code>f.truncate()</code> doesn't change the size of the file, but only the size of the data in the file.
How can I truncate the file and keep the <code>mmap</code> object valid?


A:

You can't. The <code>mmap</code> object is tied to the file size.
You can, however, create a new <code>mmap</code> object after truncating the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

