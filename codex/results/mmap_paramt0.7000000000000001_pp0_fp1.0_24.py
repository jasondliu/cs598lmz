import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))

    m.write(b'\x01')
    m.seek(0)
    print(m.read(1))
</code>
If you are trying to use this file in another process, the other process needs to have the file open in order to access the mapped region.  If you want to create a shared memory region that can be used by multiple processes, you should use <code>mmap.mmap(0, ...)</code> with a zero file descriptor, instead of opening the file yourself and passing its descriptor.

