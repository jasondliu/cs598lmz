import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m.write(b'2')

print(open('test', 'rb').read())
</code>
But this code will cause a segfault (tested on OS X, with Python 2.7.10). Printing <code>m</code> shows that the object is still valid, but the <code>mmap.write</code> call causes the segfault.
If you have a little more control over the file, you can create a file that is 5 bytes long (one byte per digit will be enough), then map the last byte of the file into memory, and write the output to that last byte:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(5))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE,
        offset=4)
    m.write(b'2')

print(open('test', 'rb').read())
</
