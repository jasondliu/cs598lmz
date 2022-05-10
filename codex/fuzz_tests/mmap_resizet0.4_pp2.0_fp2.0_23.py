import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b''
</code>
I expected to get <code>b'\x01'</code> instead.
I can't use <code>mmap.ACCESS_READ</code> because I need to read and write from the file.
I can't use <code>mmap.ACCESS_WRITE</code> because I need to read from the file.
I can't use <code>mmap.ACCESS_COPY</code> because I need to write to the file.
So, is there a way I can read from the file after truncating it?


A:

<code>mmap</code> doesn't know about the truncation. It's just a memory map of the file, and the file is still the same size.
You can either use <code>mmap.ACCESS_WRITE</code> and write a bunch of zeros over the old data, or you can use <code>mmap.resize()</code> to tell the <code>mmap</code> that the file is smaller.

