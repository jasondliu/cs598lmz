import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(type(a))
print(a)
</code>
Output:
<code>&lt;class 'bytes'&gt;
b''
</code>

