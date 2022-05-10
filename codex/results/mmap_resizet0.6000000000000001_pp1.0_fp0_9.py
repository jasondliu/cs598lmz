import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This fails with <code>mmap.error: cannot resize a mapped or shared file</code>.  I haven't found any way to get the mmap to release the lock.  <code>del m</code> doesn't help.
I'm not sure how to fix this.  Is there a way to force the mmap object to release the lock on the file?


A:

You can force the mmap to release the lock by calling <code>mmap.close()</code> first:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
    a = m[:]
</code>

