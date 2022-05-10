import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.write(bytes(1))
    print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate(0)
    b = m[:]
    f.write(bytes(1))
    print(b)
</code>
gives
<code>b'\x00'
b'\x01'
</code>
And I can't understand why.
EDIT I have already checked the documentation and it says:
<blockquote>
<p>A mmap object also provides ways to lock regions of the mapping for shared or exclusive access.</p>
</blockquote>
I can't understand why the read returned before <code>f.truncate</code>, one is protected as the other.


A:

Here's the documentation for <code>mmap.mmap</code>:
<blockquote>
<p>Memory-map a file, using an existing file descriptor fd. If size is omitted then the size of the file is used to create a file-sized mm
