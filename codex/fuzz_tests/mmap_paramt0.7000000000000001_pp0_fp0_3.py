import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print("mmap:", m.read())
    m.seek(0)
    m.write(b'\x01')
    m.close()
</code>
This works just fine:
<code>mmap: b'\x01'
</code>
But I really want to be able to write directly to a byte of a file, without having to use a <code>mmap</code> object. I would like to be able to do something like:
<code>with open('test', 'r+b') as f:
    f[0] = b'\x01'
</code>
But <code>f[0] = b'\x01'</code> doesn't work.
Is there a way to do this without using <code>mmap</code>?


A:

You can use the <code>seek</code> method of the file object to move around in the file.
<code>with open('test', 'r+b') as f:
    f.seek(0)
    f.write(b'\x01')
</code
