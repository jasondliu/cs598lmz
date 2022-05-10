import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In Windows, <code>a</code> is <code>b'\x00'</code>.
But in Linux, the mmap object will raise an exception if we try to read the file:
<blockquote>
<p>mmap.error: [Errno 9] Bad file descriptor</p>
</blockquote>
This is because, in Linux, the <code>mmap</code> object will hold the file descriptor, but in Windows, it holds the file contents.
Can I get the same behavior in Linux?


A:

As far as I know, the Linux kernel doesn't support the Windows-style memory mapping you're trying to use.
Under normal circumstances, the file is mapped into the process's virtual address space through the page cache. If the file is modified, it's copied out of the process's pages, the file is modified, and the process's pages are re-populated from the file.
In Windows, the memory mapping of a file is represented as a separate data structure from the file itself, which is what allows it to support the behavior you're looking for. Specifically, the mapping is represented by a kernel object
