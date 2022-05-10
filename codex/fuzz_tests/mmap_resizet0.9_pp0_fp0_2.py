import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It throws an exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
After the truncate, the mmap seems invalid. But I can't re-mmap it.
So how to mmap the file?
I have tried to close the file before mmap, but I have to get the file descriptor with <code>os.dup</code>, which does not work on Windows and even on Linux seems unstable. 

