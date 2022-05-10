import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The result is <code>b'\x00'</code>, but I expect <code>b'\x01'</code>.
How can I get the expected result?


A:

The problem is that you're not actually truncating the file. You're truncating the file descriptor, but the file descriptor is not the file.
The file descriptor is a handle to the file, and it has a position in the file. When you truncate the file descriptor, you're telling the OS to set the position to the end of the file.
The mmap object, however, is not affected by this. It's still pointing to the same memory, which is the same memory that was in the file before you truncated it.
You can fix this by calling <code>m.resize(0)</code> after truncating the file descriptor.

