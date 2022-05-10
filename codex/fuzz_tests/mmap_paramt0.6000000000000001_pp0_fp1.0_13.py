import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
    m.close()
</code>
The problem is that <code>m[0]</code> is not modified.
I have used this to modify a file in the past:
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
    m.close()
</code>
But this time I want to also change the file size.
Thanks!


A:

I'm not sure if this is exactly what you're looking for, but you can use <code>os.truncate</code> to set the file size:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    os.truncate(f.fileno(), 0)
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
