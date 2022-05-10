import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] #a is `bytes` object contain "b'\x00'"
</code>
OR
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    map = mmap.mmap(f.fileno(), 0)
    f.seek(0,0) #go to begin file
    f.truncate()
    a = f.read() # a is `bytes` contain ""
</code>

