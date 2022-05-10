import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\0'
</code>
But I would like to do this without creating a file on disk. I've tried using <code>io.BytesIO</code> but it doesn't seem to work with <code>mmap</code>.
<code>import io

with io.BytesIO(bytes(1)) as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\0'
</code>
Is there a way to do this?


A:

You can use <code>mmap.mmap</code> with a file descriptor obtained from <code>os.open</code> and <code>os.O_TMPFILE</code>:
<code>import mmap
import os

fd = os.open('/dev/shm', os.O_TMPFILE | os.O_RDWR)
m = mmap.mmap(fd, 1)
m[0] = b'\0'
</code>

