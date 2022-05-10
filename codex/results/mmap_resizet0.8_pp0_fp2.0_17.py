import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
Output:
<blockquote>
<p>b'\x00'</p>
</blockquote>

I know that I can use <code>mmap.ACCESS_READ</code>, but I'm curious if there is a way to do that without creating a new <code>mmap</code> instance.

