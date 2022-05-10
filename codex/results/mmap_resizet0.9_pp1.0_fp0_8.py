import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close();
</code>
Related, the docs say that:
<code>When all file descriptors and references to objects of this type are closed or the object is unmapped, the underlying file is closed
</code>
Isn't the underlying file closed first/automatically? Otherwise how can the memory map be unmapped?
Here we get <code>IOError: [Errno 1] Operation not permitted</code> if we don't close the map first.
The reason I'm not closing the map immediately is that I'm using this in a mutexed zone and I'd rather not have to reopen it every time to get a new mutex on it.


A:

It is not a bug, but an internal optimization. When the file is opened for writing, the underlying file descriptor is only closed now.  But if the file is opened readonly, the descriptor is immediately closed and the file is only closed when the MMap object is deleted.  Because in the OP code, the file is opened for writing, it is affected by the bug.
The following code, which opens the file as readonly, works as expected on all systems.
<code>
