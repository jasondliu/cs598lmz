import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

m.close()
</code>
I expect this to print out some sort of error, but it just closes without any errors.


A:

You are not seeing an error because a closed file descriptor is a perfectly valid integer. The <code>mmap</code> module does not care about the state of the underlying file descriptor, it operates on a copy of it.
The <code>mmap</code> module actually has a <code>flush</code> method you must call to have your changes saved to the file. 

