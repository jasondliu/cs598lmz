import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    time.sleep(2)
    m.resize(100)
</code>
After execution I get:
<code>OSError: [Errno 22] Invalid argument
</code>
It looks like m.resize(100) breaks things. Is there an explanation for this?


A:

You're calling <code>resize</code> on the memory mapped object. It has no way of telling the other file object that the file has been resized. You'd have to resize the file object itself.
<code>m = mmap.mmap(f.fileno(), 0)
f.truncate()
m.resize(100)
</code>

