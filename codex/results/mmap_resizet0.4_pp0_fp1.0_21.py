import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>
<code>m</code> is a <code>mmap</code> object, and <code>m[:]</code> is supposed to return the content of <code>m</code>.
Why does it return <code>b'\x00'</code> rather than <code>b'\x01'</code>?
I am using Python 3.6.9 on Ubuntu 18.04.


A:

The <code>mmap</code> object is a view into the file. The file is still open, so the operating system does not actually remove the data from the file yet.
If you close the file, the operating system will remove the data from the file, and you will see <code>b'\x00'</code> from the <code>mmap</code> object.

