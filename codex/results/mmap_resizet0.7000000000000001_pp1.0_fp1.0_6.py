import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>


A:

You're altering the file that you're mmaping, and the mmap isn't being updated. 
If you want to keep the mmap, don't close the file. 
If you want to close the file and keep the mmap, use <code>mmap.resize</code> to update the size of the mmap. 

