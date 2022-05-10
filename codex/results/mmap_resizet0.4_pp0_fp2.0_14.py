import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints <code>b'\x01'</code>, but I expect it to print an empty byte string.
I think this is a bug in <code>mmap</code> because it's not documented that <code>mmap</code> objects can be invalidated by truncation.


A:

The documentation says:
<blockquote>
<p>If the file size is increased, the bytes between the old and new ends of the file are read as zero.</p>
</blockquote>
So the behavior you see is correct.

