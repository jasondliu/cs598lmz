import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # &lt;-- 'ValueError: mmap offset is greater than file size'
</code>
Why does the <code>ValueError</code> occur? I don't expect <code>m[:]</code> to block, as the solution in https://stackoverflow.com/a/23573863/397334 suggests. Is there any way to solve this without re-acquiring a <code>mmap</code>?


A:

Looks like a bug in Python. The code throws the error even when the memory mapped region is not the last byte in the file.

