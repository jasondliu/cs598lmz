import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m[:] = b''
    b = m[:]
</code>

Why do I need to manually truncate the file after calling <code>m[:] = b''</code>?
After calling <code>m[:] = b''</code> why does <code>a</code> contain the single byte, but <code>b</code> is an empty string?
Are there any other short-comings from the memory-mapped file interface that I should be aware of?



A:

<blockquote>
<p>Why do I need to manually truncate the file after calling m[:] = b''?</p>
</blockquote>
You don't. The mmap object remains unchanged, and <code>m[:] = b''</code> is equivalent to a <code>resize</code> system call on Unix, which has no effect on mmaps other than the newly resized file.
<code>m</code> is not a fixed-size object you are copying to. The data can grow and the kernel will accomodate. The Python object just gives you an interface to the mmap.
