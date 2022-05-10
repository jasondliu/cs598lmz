import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The issue is that the <code>mmap</code> object's <code>__len__</code> method returns the old length of the file, not the new length.
The <code>mmap</code> object is supposed to be a view of the file, so if the file is truncated, the <code>mmap</code> object should be truncated as well.
The documentation says that the <code>mmap</code> object is read-only, but that's not true. You can use <code>mmap.mmap.write</code> to write to the file. The <code>mmap</code> object is just not resizable.
The documentation also says:
<blockquote>
<p>It is also possible to create an mmap object from an existing file descriptor using the mmap constructor. This only works for a file opened for reading.</p>
</blockquote>
This is not true either. If the file is opened for reading, you can't write to it, but it doesn't prevent you from using <code>mmap.mmap.resize</code>.
Is there a way to
