import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError: mmap offset is greater than file size</code>.
I tried to <code>m.resize(0)</code> before truncating the file, but it doesn't work.
Is there a way to truncate the file and keep the mmap object alive?


A:

I think your problem is that you're trying to read from the mmap object after truncating the file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    #a = m[:]
</code>
This works fine.

