import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When executing the last line it returns b'\x01' instead of b'' as I'd expect. Why does this happen and is there a way to always get an empty byte array after calling truncate (without flushing the memory map)?
As I understand, truncate is supposed to create a new file with the same name and a length of 0 and should thereby clear everything in the original file. However, since I've mmapped that file and the original file still exists (at least after the call to truncate) the process should be able to read the original version with everything in it.

