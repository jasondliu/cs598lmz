import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x0'
    m[1] = b'\x0'
    m[2] = b'\x0'
    m[3] = b'\x0'
    m[4] = b'\x0'
    m[5] = b'\x0'
    m[6] = b'\x0'
    m[7] = b'\x0'
</code>
The above code will produce a file of size 8. What is the best way to have a file of size 1 and all the other bytes as 0's? 


A:

You can use the <code>os</code> module to set the file size:
<code>with open('test', 'wb') as f:
    os.ftruncate(f.fileno(), 1)
</code>
See the docs for <code>os.ftruncate</code>: http://docs.python.org/2/library/os.html#os.ftruncate

