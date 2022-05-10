import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
</code>
I expect the output to be <code>0 0</code> but it is <code>1 0</code>.
Is this behavior expected? If so, why?


A:

The <code>mmap</code> object is not tied to the file object.  It is tied to the file descriptor.  Even if you close the file object, the <code>mmap</code> object will still be valid.  (The file descriptor is still open.)
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

fd = os.open('test', os.O_RDWR)
m = mmap.mmap(fd, 0)
a = m[:]
print(len(a))

os.close(fd)


