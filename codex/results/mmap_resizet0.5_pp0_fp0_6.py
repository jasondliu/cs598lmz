import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect this to print <code>b'\x01'</code> but instead it prints <code>b''</code>
I know that this works:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>
but I don't want to call <code>resize</code> because I want to keep the file open for writing.
Is there some way to make <code>m[:]</code> return the correct value?


A:

The behavior you're seeing is expected. From the <code>mmap</code> doc:
<blockquote>
<p>If the file on disk is smaller than length, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is extended to contain length bytes. <strong>This does not change the size of the underlying file on disk</
