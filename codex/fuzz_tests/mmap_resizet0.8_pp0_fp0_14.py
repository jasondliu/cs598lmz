import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.resize(100)
    m[0] = bytes(1)
    m[1] = bytes(1)
    m[2] = bytes(1)
    b = m[:10]
    print(b)
    print(m[0], m[1], m[2])
</code>

<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    print(m[0], m[1], m[2])
mmap.error: [Errno 22] Invalid argument
</code>
I thought m.resize() would only affect the original file, but it also changed the content of mmap object m. I would like to know why, and how can I resize the original file without changing mmap object m?

