import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the <code>mmap</code> object would be updated to reflect the new file size.
Is there a way to make this work?


A:

The <code>mmap</code> object is not updated to reflect the new file size.
The <code>mmap</code> object is a view of the file at the time it was created.
If you want to update the <code>mmap</code> object, you need to create a new one.

