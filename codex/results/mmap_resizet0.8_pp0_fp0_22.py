import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will cause a <code>ValueError</code>, because <code>m[:]</code> tries to return a slice of length 1, which is not possible since the file has been truncated to length 0.
Is there any way to avoid this race condition without installing a special module like <code>mmapfile</code>?
(A solution like "read the file into a <code>bytearray</code>" is not possible, because the file can be very large.)
Test environment: Windows 7, Python 3.4.2, <code>mmap</code> from <code>mmapfile</code> 1.0.


A:

You can just check if the map size is smaller than the buffer size you have requested:
<code>if len(m) &gt; buffer_size:
    a = m[:buffer_size]
</code>

