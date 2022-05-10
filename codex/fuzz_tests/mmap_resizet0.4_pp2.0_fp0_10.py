import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: mmap length is zero</code>.
The problem is that the mmap is still pointing to the old location in the file. I can't find any way to get it to point to the new location.
Is there a way to do this?

