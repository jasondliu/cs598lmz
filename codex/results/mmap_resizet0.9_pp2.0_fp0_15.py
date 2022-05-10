import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print('a:', a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(4)
    m[:] = bytes(4)
    m.resize(1)
    f.truncate()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 4)
    a = m[:]
    m.close()
print('a:', a)

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(4)
    a = m[:]
    f.truncate()
    b = m[:]

print('a:', a)
print('b:', b)
</code>
Output:
<code>a: b'\
