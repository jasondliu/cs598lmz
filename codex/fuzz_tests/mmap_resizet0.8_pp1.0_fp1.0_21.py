import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Why is this not throwing an <code>mmap.error</code>? According to the documentation, it should:
<blockquote>
<p>On Unix, if the underlying file is truncated or shrunk, the contents of the mmap’d region above the new end of the file are discarded</p>
</blockquote>
My test was on OSX 10.9.3, but I am afraid this is not an OS specific problem.


A:

The problem is that the <code>mmap.mmap</code> takes the second argument <code>length</code> as an upper bound for the size of the memory map in bytes. If you want to map the whole file, you can use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> or just simply <code>mmap.mmap(f.fileno())</code>.

