import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.close()
</code>
The file <code>test</code> is not updated.
If I use <code>mmap.mmap(f.fileno(), 1)</code>, the file is updated, but I don't want to specify the size (I want to use the current file size).
How can I do that?


A:

If you do not specify the length, you need to call <code>msync</code> to flush the changes to disk:
<code>m = mmap.mmap(f.fileno(), 0)
m.write(bytes(2))
m.flush()
m.close()
</code>

