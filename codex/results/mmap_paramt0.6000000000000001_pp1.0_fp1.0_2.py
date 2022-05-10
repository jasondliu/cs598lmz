import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I get
<code>b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
</code>
<code>mmap.resize</code> does not zero out the extra bytes.

<code>mmap.mmap</code> is documented to accept a <code>size</code> parameter.
<blockquote>
<p>If <em>size</em> is not 0, the file is truncated to that size and the <em>map</em> contains exactly <em>size</em> bytes.</p>
</blockquote>
This documentation is accurate.
<code>mmap.resize</code> is documented to accept a <code>new_size</code> parameter.
<blockquote>
<p>Resize the memory map to new_size bytes. The memory contents of the resized region are undefined.</p>
