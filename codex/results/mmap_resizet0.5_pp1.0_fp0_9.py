import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code>.
I know that this is because the file has been truncated, but I don't know how to fix it.
I don't want to close the file, because I don't want to lose the mmap.
I also don't want to close the mmap, because I don't want to lose the file.
I could reopen the file and mmap it again, but I'd rather avoid that.
I could seek in the mmap, but I don't know how to get the new size of the file.
How can I get the new size of the file without closing the file or the mmap?


A:

<code>mmap</code>'s <code>resize</code> method will do this for you.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.
