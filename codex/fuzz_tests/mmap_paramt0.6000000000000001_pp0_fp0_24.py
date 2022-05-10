import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')

with open('test', 'rb') as f:
    print(f.read())

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0:1].decode())
</code>
The first time, I open a file and write a byte, then I open it again and change that byte. The file is not written to disk until I close it, so the output is:
<code>b'\x01'
</code>
The second time, I open the file with mmap, and then I read the byte. The output is:
<code>\x00
</code>
Why is the byte changed when I open the file with mmap?


A:

So, I found the answer. According to the docs:
<blockquote>
<p>If a file is opened for update with access mode 'w', 'r+', or 'a' (see below), the file may be used for reading and writing. If a file is opened for update
