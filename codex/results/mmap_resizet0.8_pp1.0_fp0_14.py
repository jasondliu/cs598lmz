import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # After f.truncate() points to '\0'
    m.close()
    print(a)
</code>
Output:
<code>b'\x00'
</code>

