import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file has been truncated, but I don't understand why the <code>mmap</code> object is still trying to access the file.
Is there a way to make this code work?


A:

The <code>mmap</code> object is still trying to access the file because it is still mapped.
<code>mmap.mmap</code> has a <code>close</code> method that you can call to unmap the file.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = m[:]
</code>

