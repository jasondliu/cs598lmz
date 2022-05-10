import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me a <code>ValueError: mmap offset is greater than file size</code>.
But if I change the <code>m = mmap.mmap(f.fileno(), 0)</code> to <code>m = mmap.mmap(f.fileno(), 1)</code>, it works.
Why is that?


A:

The <code>mmap</code> module uses the <code>length</code> argument to determine the size of the file at the time the <code>mmap</code> object is created. If you pass <code>0</code> as the <code>length</code> argument, the size of the file at the time the <code>mmap</code> object is created is <code>0</code>, so the <code>mmap</code> object has no memory to map.
If you pass <code>1</code> as the <code>length</code> argument, the size of the file at the time the <code>mmap</code> object is created is <code>1</code>, so the <code
