import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

with open('test', 'r+b') as f:
    print(f.read())
</code>
The output is:
<code>b'\x02'
b'\x02'
</code>
So it seems that the memory map is not a view into the file, but rather a copy of the file.
Is there a way to get a memory map that is a view into the file?


A:

<code>mmap</code> is not a view into the file, but rather a view into the file's data in the OS's page cache. This is what allows it to be shared between processes.
If you want a view into the file, use <code>mmap.PROT_READ</code> and <code>mmap.PROT_WRITE</code> to create a read-write mapping. The data will be read from the file and written back to the file when the mapping is closed.

