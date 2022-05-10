import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Which results in <code>ValueError: mmap cannot extend file</code>. It seems like the <code>mmap</code> object is keeping the original file metadata behind the scene. Could someone please explain this? Thanks.


A:

It's not the <code>mmap</code> object doing that, that's the file object itself. An mmap object uses the OS's <code>mmap</code> API to map a file into a process' address space. It never touches the file itself.
If a file has a length of 0, there's no storage space for an mmapped bit of memory. You can't map a file that has nothing in it, nor can you use <code>malloc</code> to allocate 0 bytes of memory. The size of the memory map is fixed (technically it this trivial example it's fixed to 1, not 0). 
The size of the memory map only changes when you write to it, or unmap it and then map it again with a different size. This does not involve the file, at all; it's purely a virtual memory thing.
If you wanted to, this code would work:
<
