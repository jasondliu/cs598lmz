import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))

with open('test', 'r+b') as f:
    print(f.read(1))
</code>
I expected to see <code>b'\x02'</code> printed twice, but instead I see <code>b'\x01'</code> printed twice.
Why is this?


A:

The <code>mmap</code> object is a view of the file, not a copy of the file.  When you write to the <code>mmap</code> object, you are writing to the file.  When you read from the file, you are reading from the file.  The <code>mmap</code> object is not a separate copy of the file.

