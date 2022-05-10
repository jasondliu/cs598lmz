import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This fails with <code>ValueError: mmap offset is greater than file size</code>.
I understand why it fails, but I don't understand why it fails.  I thought that the <code>mmap</code> object would be aware of the truncation and adjust itself accordingly.  I was hoping that I could do something like this:
<code>m.truncate()
a = m[:]
</code>
Is there a way to do this?


A:

Try this:
<code>m.resize(0)
</code>

