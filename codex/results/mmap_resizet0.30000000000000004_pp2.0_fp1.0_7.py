import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in a <code>ValueError: mmap offset is greater than file size</code> exception.
This is because the file size is 0 (as a result of the truncate) but the mmap object still thinks the file is 1 byte long.
Is there a way to update the mmap object to reflect the new file size?
I know I can create a new mmap object but I'm wondering if there is a way to update the existing one.


A:

I don't think there is a way to do this.  I think the only way to do this is to close the file and open it again.  You can do this by calling <code>m.close()</code> and then <code>mmap.mmap(f.fileno(), 0)</code> again.

