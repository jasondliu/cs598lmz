import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.close()
</code>
After running this code, the file test will have the value <code>02</code>, not <code>02</code> as I would expect.
I could use something like <code>bytes(1) + bytes(2)</code> but I don't want to do that.
I am using Python 3.6.7.

