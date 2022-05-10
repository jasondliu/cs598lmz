import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # blocks here
</code>
This is the kernel bug that appears to be relevant, but it's from 2009.
It seems like you could get around the problem by using <code>os.msync()</code> before calling <code>truncate</code>, but I'm not aware of any interface for doing this.


A:

The problem is that <code>truncate(2)</code> doesn't actually truncate the file. It only makes it so that the EOF marker is earlier than it was before the <code>truncate(2)</code> call.
But then there is a race condition between <code>truncate(2)</code> and the next access. If the access happens before <code>truncate(2)</code> propagates to all the other CPUs, it will see the old file size and thus it will be blocked.
This is especially visible when you have <code>mmap(2)</code> (or any other memory mapping) from that file, because <code>mmap(2)</code> doesn't access the file contents, it just reads the metadata about the file and gets blocked. If you were
