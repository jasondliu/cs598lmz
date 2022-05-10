import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'
    m.close()
</code>
This code works fine and changes the byte in the file.
But if I change the <code>bytes(1)</code> to <code>bytes(10)</code>, the code will fail with <code>ValueError: cannot modify size of memory map</code>.
I can't understand why it happens.

