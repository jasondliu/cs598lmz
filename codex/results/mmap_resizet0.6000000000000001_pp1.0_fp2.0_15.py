import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line will raise an exception:
<code>ValueError: mmap offset is greater than file size
</code>
Can you please explain why?


A:

The <code>mmap</code> object is not updated to reflect the new size of the file. 
The <code>mmap</code> object is basically a view into the underlying file. It doesn't matter that you truncated the file, the <code>mmap</code> object still thinks the file is the same size. 

