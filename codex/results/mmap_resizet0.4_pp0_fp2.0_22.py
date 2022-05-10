import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the <code>a</code> to be empty, but it is <code>b'\x01'</code>


A:

<code>mmap</code>'s <code>mmap</code> function takes a <code>length</code> parameter, which is the size of the mapping.  If you set it to 0, it will use the current size of the file.  So, when you call <code>mmap</code>, the file is 1 byte long, and the mapping is 1 byte long.  When you call <code>f.truncate()</code>, the file is truncated, but the mapping is still 1 byte long.  So, <code>m[:]</code> returns the 1 byte that used to be in the file.
If you want the mapping to be the same size as the file, you need to call <code>mmap</code> with a <code>length</code> parameter that's the size of the file.  For example, you could do
<code>m = mmap.mmap(f.fileno(), os.fstat(f.
