import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand why this happens, but I don't understand why the <code>mmap</code> object is not updated when the file is truncated.
I would expect <code>a</code> to be an empty byte string.
Is there a way to update the <code>mmap</code> object after truncating the file?


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.  It is a view of the file as it was when you created it.  If you want to update the <code>mmap</code> object, you need to create a new one.

