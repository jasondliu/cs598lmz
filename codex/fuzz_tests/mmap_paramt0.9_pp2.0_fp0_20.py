import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
My impression is that the last <code>m.close()</code> does not close the file. I thought it does because the second example here shows that the same <code>m.close()</code> call releases the lock on the file.
Minimal example to demonstrate the problem:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
    f.write(bytes(1))  # Raises UnsupportedOperation: not writable
</code>
I'm using Python 3.6.2 on Windows 7.

