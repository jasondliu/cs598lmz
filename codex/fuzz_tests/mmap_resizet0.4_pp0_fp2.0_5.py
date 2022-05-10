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
I expected the output to be <code>b'\x01'</code>, but it is <code>b''</code>.
The documentation says:
<blockquote>
<p>The mmap object is not usable after this call, but the file descriptor fd is still open.</p>
</blockquote>
However, the file descriptor is not open, as the file is closed.
What is the correct way to truncate a file while keeping the mmap open?

