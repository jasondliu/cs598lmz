import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)

print(m)
</code>
I printed out the <code>mmap</code> object and that is:
<code>&lt;mmap.mmap object at 0x7ff3922482d0&gt;
</code>
If I wanted to write to the file after closing it. What would I need to do?
My goal is to append data to a file without having to load it in RAM.


A:

Use the <code>mmap.mmap.seek()</code> methods to move from the zero-offset to the end of the file, then use <code>mmap.mmap.write()</code> to append what you need.
Note that you need to open the file in read-write mode first, else when you close the file it may be truncated.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print('first byte: ', m[0])
    m
