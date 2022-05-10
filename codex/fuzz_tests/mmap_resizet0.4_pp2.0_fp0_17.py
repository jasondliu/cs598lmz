import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It prints <code>b'\x01'</code> and I was expecting <code>b''</code>.
Why does it print <code>b'\x01'</code>?


A:

<code>mmap</code> is a memory map of the file, and is not affected by the file size. It will continue to show the contents of the file at the time the <code>mmap</code> was created, even if the file is truncated.
If you want to truncate the file, you need to call <code>mmap.resize()</code> to resize the mapping; this will also change the file size.

