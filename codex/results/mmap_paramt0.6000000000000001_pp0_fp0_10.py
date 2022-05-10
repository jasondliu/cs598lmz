import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()

with open('test', 'rb') as f:
    print(f.read())

</code>
It prints <code>2</code> instead of <code>1</code>. So, I think that there is a bug in <code>mmap</code> module.
What is wrong?

