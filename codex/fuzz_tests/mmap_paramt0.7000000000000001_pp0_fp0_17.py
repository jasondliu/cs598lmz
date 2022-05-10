import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0:4] = b'wxyz'
    print(m)
    m.seek(0)
    print(m.readline())
    m.close()
</code>
Output:
<code>&lt;mmap.mmap object at 0x10b31e320&gt;
&lt;mmap.mmap object at 0x10b31e320&gt;
b'wxyz'
</code>
However, I am not sure what the "at 0x10b31e320" is in the output and if that is the same for everyone. 

