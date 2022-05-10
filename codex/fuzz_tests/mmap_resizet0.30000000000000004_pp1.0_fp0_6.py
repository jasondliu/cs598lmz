import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
This prints <code>b'\x00'</code>, which is not what I expected.
I expected the memory map to be invalidated when the file is truncated.
I'm using Python 3.5.2 on Linux.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If the file is resized or otherwise modified in a way that affects the memory mapping, behavior is determined by the <code>&lt;code&gt;access&lt;/code&gt;</code> parameter.</p>
</blockquote>
The default access mode is <code>ACCESS_DEFAULT</code>, which is defined as:
<blockquote>
<p>This is the default value and corresponds to <code>&lt;code&gt;ACCESS_READ | ACCESS_WRITE&lt;/code&gt;</code>.</p>
</blockquote>
So, the default access mode is <code>ACCESS_READ | ACCESS_WRITE</code>, which means that the
