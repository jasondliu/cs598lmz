import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception
<code>mmap.error: [Errno 22] Invalid argument
</code>
I understand the error, but I'm wondering if there is any workaround?


A:

There is no magic. <code>mmap</code> is a virtual mapping of the file into memory, so when you truncate the file, there is no way for the <code>mmap</code> object to know that the file has been truncated.
You should, instead, use <code>mmap.resize(len)</code> to resize the mapped region.

