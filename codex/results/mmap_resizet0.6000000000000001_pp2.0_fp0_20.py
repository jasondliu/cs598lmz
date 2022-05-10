import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case <code>a</code> is <code>b'\x00'</code>, but I would expect it to be <code>b'\x01'</code>. 
Why is that?
Is there a way to do this without closing and reopening the file?


A:

You can't truncate the file while the memory-mapping is still valid, as the OS has to be able to map the file to memory again.
You can, however, use <code>mmap.resize()</code> to resize the memory-mapping to the new file size (the function will return an error if the file has been truncated while the mapping is still active).

