import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x01'
</code>
But that requires you to know the size of the file beforehand, and it won't grow if you write to the end.
The right way to do it would be to create a new file with the right size, copy the data over, and then delete the old file, but that's not atomic.

