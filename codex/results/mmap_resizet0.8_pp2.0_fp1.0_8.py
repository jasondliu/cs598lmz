import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> will no longer be empty if the file were appended to before truncation. If it were truncated prior to the mmap, there is no way to know the size of the truncated data.

