import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(3))
    m.seek(0)
    print(m.read())
</code>
Output:
<code>b'\x02'
b'\x03'
</code>
Why is the value <code>3</code> not <code>2</code>? I'm not sure I understand what is happening.


A:

The reason for that is because the <code>mmap</code> is not closed after the first <code>with</code> block.
From the docs:
<blockquote>
<p>If the file is opened in read-write mode, the mmap() method can be used to write to the mapped file.</p>
<p>Changes made to the mmap object are reflected in the file itself. The mmap object also supports some limited file-like methods, including read
