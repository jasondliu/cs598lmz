import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It seems that the mmap object is still referring to the old file, and the new file is empty. Is there a way to update the mmap object to point to the new file?


A:

<blockquote>
<p>It seems that the mmap object is still referring to the old file, and the new file is empty. Is there a way to update the mmap object to point to the new file?</p>
</blockquote>
No.
The <code>mmap</code> object refers to a memory-mapped file.  Once you truncate the file, the memory-mapped file is gone.  You need to close the <code>mmap</code> object, and then open a new one.

