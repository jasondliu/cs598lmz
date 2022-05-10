import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 0
    print(m[0])
    m.close()
</code>
Output:
<code>1
0
</code>
However, I don't see any point in using <code>mmap</code> when you're going to overwrite the entire file anyway. It's just one more thing to go wrong.

