import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get: <code>b'\x01'</code> as a result

However, I tried to use same file and mmap for reading a file:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(10))

with open('test', 'r+b') as f:
    a = f.read()
    print(a)
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    b = m[:]
    print(b)
    m.close()
</code>
results:
<code>b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>

same result with file being opened as <code>'r'</code>
