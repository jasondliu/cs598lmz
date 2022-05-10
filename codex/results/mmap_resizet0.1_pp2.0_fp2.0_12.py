import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the problem is that the file is truncated and the mmap object is not aware of that.
Is there a way to make the mmap object aware of the file truncation?
I know that I can close the file and reopen it, but I would like to avoid that.
I am using Python 3.6.


A:

You can use <code>mmap.resize</code> to resize the mmap object.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

