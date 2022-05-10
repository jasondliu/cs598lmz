import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is: <code>b''</code>
What I expected is to get a <code>ValueError</code>.
I wonder why it is not an error?
I am using <code>Python 3.6.1</code> on <code>Ubuntu 16.04.2</code>.


A:

The docs for mmap say:
<blockquote>
<p>The mmap module also provides a way to map a file into memory using the <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function. This is useful for accessing small fragments of large files without reading the entire file into memory.</p>
</blockquote>
So it's not a problem that you've truncated the file. It's just that you've truncated the file to zero bytes, so there's nothing to map.

