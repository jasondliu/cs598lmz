import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.write(bytes(1)) #this raises OSError 22, Invalid argument
</code>


A:

I think it's because you are trying to write into the end of your file. Try to <code>m.seek(0, 2)</code> before the second write.

