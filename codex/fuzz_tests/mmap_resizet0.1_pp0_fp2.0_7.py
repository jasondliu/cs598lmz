import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expected the output to be <code>b'\x01'</code>.
Why is this?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file at the time it was created.
If you want to update the <code>mmap</code> object, you need to call <code>mmap.resize</code> after truncating the file.

