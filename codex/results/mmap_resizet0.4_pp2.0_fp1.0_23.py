import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Running this code gives me a <code>ValueError: cannot mmap an empty file</code> on the line <code>a = m[:]</code>.
I'm trying to understand why this is happening. I've read the documentation for mmap, and it says that <code>mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0)</code> and that the <code>fileno</code> is the file descriptor of the file to be memory-mapped.
I'm not sure what that means, but I know that the file descriptor for <code>f</code> is 3, so I'm assuming that's the file descriptor that is being passed to <code>mmap</code>.
The documentation also says that <code>length</code> is the number of bytes to map. I'm assuming that 0 means the entire file.
So, why is it that I'm getting an error when I try to access the memory-mapped file?


A:

The error is caused by the line <code>f.truncate
