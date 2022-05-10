import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in an <code>ValueError: cannot mmap an empty file</code> error. 
Python docs state that the <code>truncate</code> method is supposed to work on mmap objects. 
Is there any way to resize an mmap object?

