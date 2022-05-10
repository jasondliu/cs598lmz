import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.resize(2)

with open('test', 'rb') as f:
    print(f.read())
</code>
My assumption was that this would result in the file being 2 bytes large. However, it is still 1 byte large. I tried to look for anything in the mmap doc that would explain this behaviour, but I couldn't find anything.


A:

<code>mmap.resize()</code> only allows you to increase the size of the mapping. From the documentation:
<blockquote>
<p><code>&lt;code&gt;mmap.resize(new_size)&lt;/code&gt;</code></p>
<p>Changes the size of the mapping. If the new size is larger than the current size, the mapping is extended, and the new memory is <strong>uninitialized</strong>. If the new size is smaller, the mapping is truncated.</p>
<p>The resize operation is only possible for <code>&lt;code&gt;mmap&lt;/code&gt;</
