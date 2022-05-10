import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception:
<code>OSError: [Errno 9] Bad file descriptor</code>
Is this expected?
What I'd like to achieve is truncate the file to zero bytes but keep the mapping object <code>a</code> valid. Is this possible?


A:

The short answer is no.  The mmap.mmap object is tied to a region of memory in a file, and when the file is truncated and the region size becomes zero, the object is lost.
You could mmap the file with length 0, but I'm not sure there's much value in preserving the memory map when you have no memory mapped.  I can imagine cases where you might want to reopen and re-mmap a file that you've truncated, but I can't think of any such case where the old mmap object needs to be kept alive.

