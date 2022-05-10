import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] #here it fails
</code>
<code>mmap.error: [Errno 22] Invalid argument
</code>
Why does it happen? And how can I resolve it?
P.S. I use Windows, but it's a bit irrelevant here.

