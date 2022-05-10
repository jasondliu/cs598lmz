import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b''</code> but I expect it to be <code>b'\x01'</code>.
If I use <code>mmap.mmap(f.fileno(), 1)</code> then it works fine. I'm pretty sure this is a bug.


A:

In Linux, the mmap function is defined as:
<code>void *mmap(void *addr, size_t length, int prot, int flags,
           int fd, off_t offset);
</code>
The length argument specifies the length of the mapping.
When you used <code>mmap.mmap(f.fileno(), 0)</code>, it means you want to map 0 bytes of the file.
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is zero, the appropriate size is automatically determined.</p>
</blockquote>
However, there is no file data to map, therefore <code>m[:]</code> returns an empty string.
When you used
