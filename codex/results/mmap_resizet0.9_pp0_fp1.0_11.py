import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
with <code>mmap</code> I get an empty <code>bytearray</code>, without <code>mmap</code> a <code>bytearray</code> of length 1.
Edit:
Writing the <code>bytearray</code> via <code>write</code> works
Edit2:
When creating a file of size 1, both mmap and without mmap work.
Edit3:
On Windows, I have to call <code>mmap.MADV_DONTNEED</code> for the truncate to work.

