import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>, which is not what I expect.
I expect that <code>f.truncate()</code> will make the file empty, and <code>m[:]</code> will return an empty byte string.
I know that I can use <code>m.seek(0)</code> and <code>m.resize(0)</code> to achieve the same result, but I want to know why <code>f.truncate()</code> doesn't work.

