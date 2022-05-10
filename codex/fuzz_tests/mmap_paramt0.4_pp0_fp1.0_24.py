import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x01'
</code>
I expect the output to be <code>b'\x02'</code>.


A:

The problem is that the <code>mmap</code> object you create is 0 bytes long.
<code>mmap.mmap(f.fileno(), 0)
</code>
This is equivalent to
<code>mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
</code>
which means you can only write to the first byte of the file.
If you want to write to the whole file, you need to use the size of the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), os.fstat(f.fileno()).st_size)
    m.write(bytes(2
