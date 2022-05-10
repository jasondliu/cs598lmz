import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm pretty sure that memory mapping is not supposed to work like this. Is this a bug?


A:

The mmap module documentation states:
<blockquote>
<p>It is possible to create a read-only or write-only memory map using the access parameter. The default value is <code>&lt;code&gt;ACCESS_COPY&lt;/code&gt;</code> to create a copy-on-write mapping; this must be combined with either <code>&lt;code&gt;ACCESS_READ&lt;/code&gt;</code> or <code>&lt;code&gt;ACCESS_WRITE&lt;/code&gt;</code>.</p>
</blockquote>
To get a read-only mapping, you should do:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>

