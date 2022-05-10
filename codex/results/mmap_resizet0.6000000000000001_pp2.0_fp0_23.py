import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the error:
<code>ValueError: mmap offset is greater than file size
</code>
Why is that? And how can I fix it?


A:

When you truncate the file, you shrink it to 0 bytes.
After that, when you do <code>m[:]</code>, you're trying to read from a position beyond the end of the file.
You can either open the file with the <code>size</code> parameter:
<code>m = mmap.mmap(f.fileno(), size=1, access=mmap.ACCESS_READ)
</code>
Or you can use <code>m.resize()</code> to resize it after truncating the file:
<code>f.truncate()
m.resize(1)
</code>

