import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError</code> on the last line:
<code>ValueError: mmap length is greater than file size
</code>
However, if I replace the <code>f.truncate()</code> line with <code>f.write(bytes(1))</code>, everything works fine.
Why is this?


A:

When you truncate, the file pointer is not moved. So when you try to read from the mmap, you're trying to read from a position beyond the end of the file.
When you write to the file, the file pointer is moved to the end of the file, so when you read from the mmap, you're reading from the start of the file, which is valid.

