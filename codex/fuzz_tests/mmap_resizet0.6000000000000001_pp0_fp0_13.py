import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises a <code>ValueError</code>:
<blockquote>
<p>ValueError: mmap can't extend memory maps backed by files</p>
</blockquote>
How can I read the contents of an mmap after truncating the file?


A:

The problem is that the <code>mmap</code> object doesn't know about the truncation. It's still mapped to the original file size.
You need to close the <code>mmap</code> object first.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = f.read()
</code>

