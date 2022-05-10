import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
print(len(a))
</code>
This throws an Exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Remove the line <code>f.truncate()</code> and it works just fine.

I can avoid deleting the mutable memory map completely by using <code>posix_fallocate</code> with <code>truncate</code>:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    pos = m.tell()
    a = m[:]
    os.truncate(f.fileno(), pos)

print(a)
print(len(a))
</code>
However, this solution is mildly unpleasant.
Is there a better way?

