import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but the mmap object is still pointing to the old file size.
I have tried to use <code>m.resize(0)</code> and <code>m.close()</code> but it doesn't help.
Is there a way to truncate the file and resize the mmap object?

