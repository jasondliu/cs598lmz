import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    pos = m.tell()
    m.seek(0, os.SEEK_END)
    print(m.tell())
    print(pos)
</code>
Output:
<code>1
1
</code>
It seems that the position is always at the end of the file, regardless of whether we seek or not.
I'm using Python 3.2.2, Linux.


A:

You might try using a <code>io.BufferedReader</code> to create the <code>mmap</code> object -- its <code>tell()</code> hasn't been overridden.

