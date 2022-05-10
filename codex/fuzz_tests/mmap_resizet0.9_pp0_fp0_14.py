import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This should print <code>b'\x00'</code> but I get <code>b''</code>. The file <code>test</code> does get truncated to 0 bytes but if I print the size of the <code>mmap</code> it shows 1 byte.
Why does the <code>mmap</code> object not get updated when the file changes and how can I force a resync/reload of the <code>mmap</code> object?


A:

The <code>mmap</code> is fixed to the same length as the file when you create it, and there is no automatic extension mechanism.
<blockquote>
<p>To create a private copy of the underlying file, use <em>access=mmap.ACCESS_COPY</em>.</p>
</blockquote>
That's what you'll have to do here, and recreate the map after each <code>truncate()</code>. And you can't open two <code>mmap.mmap()</code> objects on the same file.
The background here is that
