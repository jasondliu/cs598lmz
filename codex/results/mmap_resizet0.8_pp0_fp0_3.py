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
<code>b'\x01'
</code>
How <code>1</code> can be in memory even if file is truncated? <code>test</code> is just one byte and it's full with <code>\x01</code>.


A:

When you open <code>mmap.mmap(f.fileno(), 0)</code> with 0 (zero) as the length, the mmap length will be set to the current length of the underlying file. This means that, after truncating the file with <code>f.truncate()</code> the file length is 0 and the mmap size is 0 as well. This is reflected in the fact that you get an empty byte string for m[:] since the mmap object is empty.

