import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in a <code>ValueError</code>:
<code>ValueError: mmap can't resize a readonly or copy-on-write (COW) mmap
</code>
I found a similar question here, but I don't want to use the <code>mmap.resize</code> method because I want to be able to truncate the file to 0 bytes.
I also tried to use <code>mmap.ACCESS_WRITE</code> instead of <code>mmap.ACCESS_COPY</code>, but that results in a <code>PermissionError</code>.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    f.truncate()
    a = m[:]
</code>
<code>PermissionError: [Errno 13] Permission denied
</code>
Is there any way to truncate a file to 0 bytes and then read from it using a <code>mmap</code>?
