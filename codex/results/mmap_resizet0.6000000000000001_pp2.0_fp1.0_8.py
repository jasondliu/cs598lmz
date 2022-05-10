import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the above code, the last line raises <code>ValueError: mmap offset is greater than file size</code>.
I don't understand how that can happen, as I haven't moved the cursor.

The following code works as expected:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.seek(0)
    a = m[:]
</code>
But I don't understand why the seek is necessary.

