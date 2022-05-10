import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'

print(open('test').read())
</code>
<blockquote>
<p>2</p>
</blockquote>

