import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that this is because the file size is now 0, but I don't understand why the mmap object is not updated.
I tried to use <code>m.resize(0)</code> but it raises <code>ValueError: cannot resize a mmap backed array</code>.
Is there a way to resize the mmap object?


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file, not a copy of the file.
If you want to update the file, you need to update the <code>mmap</code> object.
If you want to update the <code>mmap</code> object, you need to update the file.
If you want to update the file and the <code>mmap</code> object, you need to update the file and the <code>mmap</code> object.
If you want to update the <code>mmap</code> object
