import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is <code>b''</code> when it should be <code>b'\x01'</code>.
The problem is that the truncation is not applied to the mmap object, so the mmap object is still pointing to the old data.
Is there a way to get the updated data?


A:

I think you're misunderstanding the purpose of <code>mmap</code>.  When you <code>mmap</code> a file, you're mapping the underlying data in the file.  You're not mapping the file descriptor.  So when you truncate the file, the data in the file is truncated, but the mmap object is still pointing to the old data.
If you want to truncate the file, you'll need to unmap the file first, and then remap the file.  If you don't want to truncate the file, you'll need to leave it alone.

