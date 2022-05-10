import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE)
    m.write(b'2')
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'1'
</code>
But when I use <code>access=mmap.ACCESS_READ</code>, I can read the file, but I cannot write to it.
I did not find any documentation on this. How can I both read and write while using <code>mmap</code>?


A:

I found after digging in the documentation:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE)
    m[0] = b'2'
    m.close()
</code>

