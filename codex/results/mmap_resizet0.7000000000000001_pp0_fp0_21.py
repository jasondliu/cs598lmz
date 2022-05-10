import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

with open('test', 'wb') as f:
    f.write(bytes(2))
</code>
The last line will fail with <code>ValueError: mmap can't resize file to smaller size</code>.
I would like to understand why mmap prevents operating system to do this.


A:

There are two different issues:

Cannot resize the file to a smaller size than the current size of the mapped region. This is because the data in the file is still there (until you close the mapping), so it will still be there when you reopen the file.
Cannot write to a region that is mapped. That's because the data you write gets written to the memory-mapped area, not to the file.

You can resize the file to a larger size, but that will not affect the mapping you have open. Only the portion of the file that is mapped will be visible in the mapping.

