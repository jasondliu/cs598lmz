import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that this is because the file is truncated and the offset is now greater than the file size.
But I don't understand why the offset is not updated when the file is truncated.
Is there a way to update the offset?
I'm using Python 3.5.2 on Windows 10.


A:

The <code>mmap</code> object is not aware of the file size. It is only aware of the size of the mapping. The mapping size is not affected by <code>truncate()</code>.
If you want to truncate the file and the mapping, you need to call <code>mmap.resize()</code> after <code>truncate()</code>.

