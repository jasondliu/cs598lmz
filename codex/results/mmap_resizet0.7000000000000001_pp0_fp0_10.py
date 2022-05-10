import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be an empty string, but instead it's <code>\x01</code>.
Why does the truncate function not affect the mmap object? 


A:

<code>f.truncate()</code> doesn't clear the file (and therefore, <code>mmap</code>). It just changes the size of the file to <code>0</code>, and the <code>mmap</code> is still valid.
<code>f.truncate()</code> has the same effect as <code>os.truncate(f.fileno(), 0)</code>.
To clear the file, you can do:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.seek(0)
    f.write(bytes(0))
    m.flush()
    a = m[:]
</
