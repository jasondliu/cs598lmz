import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    print(len(a))
</code>
The output is both the <code>len(a)</code> and the <code>print(a)</code> are <code>b''</code>. If I change the <code>0</code> to <code>1</code> then the output is an <code>IndexError</code>.
How do I get the mmap to contain the bytes that were in the file before the truncation?


A:

<code>mmap</code> is only a view of the underlying file. If you truncate the file, the view is no longer valid.
You can avoid the truncate call, by using the <code>mmap.resize()</code> method instead:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
    print(a)
    print(len(a))
</code>
This will resize the mmap object, not the underlying file. The file size
