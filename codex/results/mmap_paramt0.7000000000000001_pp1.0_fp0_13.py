import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0x02
</code>
It works. But what if I want to map only a small portion of the file?
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, offset=1)
    m[:] = bytes([0x03])
</code>
The last line causes an error. The same error happens if I set <code>offset=0</code> and use <code>m[0] = 0x01</code> instead of <code>m[:] = bytes([0x03])</code>.
I understand that I am mapping only a single byte, so I cannot write <code>bytes([0x03])</code> to it. But why can I not write a single byte to it?
Is it possible to map a single byte of a file in Python?


A:

You're trying to write in a buffer that overflows the memory mapping, so it's not possible. Even if you use <code>m[0]</code>, you're trying to write a single byte in a
