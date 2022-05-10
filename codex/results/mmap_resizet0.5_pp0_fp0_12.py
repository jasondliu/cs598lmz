import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Error:
<code>mmap.error: [Errno 9] Bad file descriptor
</code>
I also tried:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.flush()
    f.truncate()
    a = m[:]
    m.close()
</code>
Error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
What is the correct way to do this?


A:

<code>m = mmap.mmap(f.fileno(), 0)
</code>
This is not a valid call to <code>mmap.mmap</code>.  The second argument to <code>mmap.mmap</code> is the length of the memory map.  If you pass a length of 0, you get an error.
You should pass the size of the file in the second argument.  If you don't know the size of the file, you can use <code>
