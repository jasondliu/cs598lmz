import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 5
    m.close()

with open('test', 'rb') as f:
    data = f.read()
    print(data)
</code>
Output:
<code>b'\x05'
</code>

If you want to write multiple times, you can do this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 5
    print(m[0])
    m[0] = 10
    print(m[0])
    m.close()

with open('test', 'rb') as f:
    data = f.read()
    print(data)
</code>
Output:
<code>5
10
b'\n'
</code>

