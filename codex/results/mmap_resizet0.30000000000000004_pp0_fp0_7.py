import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>b''</code>, but instead it is <code>b'\x01'</code>.
I am running Python 3.6.1 on Windows 10.


A:

This is a known issue with the Windows implementation of <code>mmap</code>.
<blockquote>
<p>The Windows implementation of mmap() is very limited. It is only capable of creating mappings on whole pages in the virtual address space of the process. The granularity of the offset argument is the system allocation granularity, which is the size of a memory page. The size argument must be an integral multiple of the allocation granularity. The offset argument must be a multiple of the allocation granularity. The PROT_WRITE and PROT_EXEC flags are not supported. The MAP_PRIVATE flag is not supported for fixed mappings.</p>
</blockquote>
https://docs.python.org/3/library/mmap.html#mmap.mmap

