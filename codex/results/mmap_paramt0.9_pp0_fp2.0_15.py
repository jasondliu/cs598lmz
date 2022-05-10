import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    for a in range(1, 2**8):
        m[0] = a
</code>
First try:
<code>    for a in range(1, 2**8):
        mm = mmap.mmap(f.fileno(), 0)
        mm[0] = a
        mm.close()
</code>
produces <code>mmap.error: [Errno 22] Invalid argument</code>. So I thought it could be this page:
<blockquote>
<p>When you're done with a mmap object, close it as you would close a regular file. ... Closing a mmap is only required when you intend to destroy the mmap object or make it inaccessible.</p>
</blockquote>
My first try would assume I'd need to call <code>close</code>, but the documentation says I do not, which is also confirmed by the second try:
<code>    for a in range(1, 2**8):
        mm = mmap.mmap(f.fileno(), 0)
        mm[0] = a
</code>
So which version is
