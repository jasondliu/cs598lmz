import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 65
    m.close()
</code>
But this, which I thought would be equivalent, doesn't work.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 65
    m.close()
</code>
I get a ValueError that it can't write to the memory-mapped file. Is there some reason for this or am I missing something?


A:

In your first approach you're creating a new file (<code>wb</code>) so it's read/write. But in the second approach you're opening an already existing file (<code>rb</code>) so it's read-only. In other words: the file was created read/write, but in the second approach you're opening it read-only.
I can't see that in the documentation but it makes sense to me: a file is read-only or read-write, and once a file is created and opened it
