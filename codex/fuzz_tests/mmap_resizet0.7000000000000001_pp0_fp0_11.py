import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The above code gives me a segfault. How do I avoid this?


A:

The documentation is surprisingly clear about this:
<blockquote>
<p>The underlying file may grow in size, but may not shrink. When the file does grow, the extra memory is uninitialized; it behaves as if you had written zeros to that region.</p>
<p>The *len* argument specifies the initial size of the mapped region; this may be larger than the file size. The optional *access* argument controls the type of access (assuming the OS supports it)</p>
</blockquote>
So you can't shrink the file and keep your mmap instance intact.
Instead, you could create a new mmap instance, and copy the bytes you want to keep over to it.

