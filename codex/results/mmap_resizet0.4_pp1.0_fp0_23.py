import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError: mmap offset is greater than file size</code> exception.
I'm trying to understand why this happens. I've read the documentation and it says that <code>mmap</code> objects are invalidated when the file is truncated. I'm not sure what "invalidated" means. Does it mean that the <code>mmap</code> object is no longer usable?
I'm trying to understand what happens to the memory mapped region when the file is truncated. I thought that the memory mapped region would be unchanged and that the <code>mmap</code> object would be invalidated because it would no longer point to a valid memory mapped region.
So why does the <code>mmap</code> object still point to a valid memory mapped region after the file is truncated? Is it because the <code>mmap</code> object is created with a length of 0, so the memory mapped region is the empty region at the end of the file?
I'm trying to understand what happens to the memory mapped region when the file is truncated. I thought that the memory mapped region would be unchanged and that the <code
