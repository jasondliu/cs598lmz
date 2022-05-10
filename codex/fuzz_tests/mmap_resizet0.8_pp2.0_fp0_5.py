import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm expecting to receive an error because I truncated the file and then read from an mmap object.
I change the code to use mmap.ACCESS_READ and get the same result:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate()
    a = m[:]
</code>
I'm using Python3.3. I've also tried to use mmap.mmap(-1, ...) and still get the same result.
What am I missing?


A:

Mechanically, you're not missing anything.
The POSIX <code>mmap</code> system call has no effect on the size of the file. It can be used to read a file that is larger than the mapped region, and the C standard library implements <code>truncate</code> so that it can be used to reduce the size of a file that
