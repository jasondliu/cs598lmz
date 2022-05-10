import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('a')

with open('test', 'rb') as f:
    print(f.read())
</code>
I'm opening a file of one byte, writing the byte <code>1</code> to it, then mmap-ing that file, changing the byte to <code>a</code>, and finally reading the file back.
The output is:
<code>b'a'
</code>

