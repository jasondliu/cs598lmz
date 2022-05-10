import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read(1))
</code>
In this example, I open a file for writing, write a single byte to it, then open it for reading and writing, mmap it, write a second byte to it, and then close the mmap. In the end, I open it for reading and expect to see both bytes.
What happens, on the other hand, is that only the second byte is returned when I try to read from the file. If I open it for writing, the first byte is overwritten and the second is left in place.
Python documentation says that writing to a mmap object "copies the bytes object b to the mmap object", which is what I'd expect it to do. 
What is wrong here? Did I misunderstand the documentation? Will I have to manually get the old bytes and merge them with the new one?
Here is a minimal example that should be able to reproduce the error, assuming <code>ascii.txt</code> (and <code>abc.txt</code>) exists
