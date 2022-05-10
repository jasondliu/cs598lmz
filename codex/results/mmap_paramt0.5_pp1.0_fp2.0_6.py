import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m[0])
    m.close()
</code>
It prints <code>2</code> as expected. But if I change it to
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m[0])
    m.close()
    print(f.read(1))
</code>
It prints <code>2</code> and then <code>1</code>. Why is the file not updated? I thought the original file would be updated when <code>m.close()</code> is called.


A:

You need to call <code>m.flush()</code> before closing the mmap object.

