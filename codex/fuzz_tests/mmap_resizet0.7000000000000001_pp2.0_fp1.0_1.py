import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The code above raises the <code>mmap.error</code> since the file is not big enough.
Is there any way to workaround this? I want to truncate the file and then get the data before truncation.


A:

Instead of
<code>m = mmap.mmap(f.fileno(), 0)
</code>
use
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>
This will allow you to read the data even if the underlying file descriptor is truncated.

