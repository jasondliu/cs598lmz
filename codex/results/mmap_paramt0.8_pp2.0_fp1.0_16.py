import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.flush()
    m.close()

os.unlink('test')
</code>
The above error is not caught by the <code>try..catch</code> block.
Question
Why does Python's mmap module ignore the <code>mmap.error</code> exception if it is caught?

