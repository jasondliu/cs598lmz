import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I have a <code>mmap</code> on a file <code>test</code> which has a single byte. I then truncate the file to zero bytes.
If I read from <code>m</code>, I get the expected <code>b''</code>. But if I read from <code>a</code>, I get <code>b'\x00'</code>.
Why does this happen?

