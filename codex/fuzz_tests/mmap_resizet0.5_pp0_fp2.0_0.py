import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to truncate the file but keep the data in memory.
I tried to do this but it doesn't work.
How can I do this?


A:

You can't.
The file is truncated when you call <code>f.truncate()</code>, and the <code>mmap</code> object is immediately invalid.

