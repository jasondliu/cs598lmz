import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be empty but it's actually <code>b'\x01'</code>. Why is that?


A:

This is a known issue in Python 3.2, and was fixed in Python 3.3. See issue #13013 for more details.
<blockquote>
<p>From <a href="https://bugs.python.org/issue13013#msg153775" rel="nofollow">msg153775</a>:</p>
<blockquote>
<p>When resizing a file, the underlying kernel file truncate operation
    and the memory mapping that it affects are not atomic. This can cause
    a race condition where the mmap sees the kernel truncate, but the
    kernel hasn't actually resized the file yet and so it is still the
    original size.</p>
</blockquote>
</blockquote>

