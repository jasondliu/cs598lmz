import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>
I expected the output to be <code>b''</code>
Why is this?


A:

The <code>mmap</code> object is not updated when the file is truncated.
From the docs:
<blockquote>
<p>The mmap object is not updated if the underlying file on disk is changed by another process.</p>
</blockquote>

