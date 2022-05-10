import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect the output to be <code>b'\x01'</code>, but I get <code>b''</code>.
I know that I can use <code>m.seek(0)</code> to get the expected output, but I don't understand why <code>m[:]</code> doesn't work.
I'm using Python 3.6.1 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the view is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the view is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the view is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the view is not updated when the file is truncated.
The <code>mmap</code
