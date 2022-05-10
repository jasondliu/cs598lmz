import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I am using Python 3.4.3 on Windows 7.


A:

<code>bytes(1)</code> creates a single-byte string, not a single-byte integer.
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
</code>
You can use <code>bytes([1])</code> instead.

