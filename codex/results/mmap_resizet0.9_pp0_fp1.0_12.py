import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[0:8]
    del m
</code>
For python 2, only <code>del m</code> is enough to prevent the error.
For python 3, we have to add <code>a = m[:]</code> and <code>b = m[0:8]</code>.


A:

According to PEP 3118 and the comment on a bug report about this issue, you can safely consume a BufWrapper (including the bytes returned from a memory map), since consuming it doesn't change the reference count on the underlying buffer, so closing the BufWrapper won't free the memory, memory mapping it won't close the underlying file, or otherwise affect the underlying object.  The only thing consuming the BufWrapper will change is that when the last reference to the BufWrapper is deleted, the <code>__del__</code> method will be called, which will call <code>free_buffer</code>.  
That method will only do anything if the object was constructed with an <code>extern_obj</code> parameter and <code>free</code> is True (which it isn't when
