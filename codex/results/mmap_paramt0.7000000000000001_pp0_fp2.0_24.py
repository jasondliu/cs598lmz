import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m[0] = b'c'
</code>
The file is opened for binary reading and writing, and the mode for mmap is also <code>ACCESS_READ|ACCESS_WRITE</code>. But the last line throws a <code>ValueError: mmap can't modify a readonly or copy-on-write memory mapping</code>.
Why is that? Why can't mmap modify the memory in this case?


A:

From the docs:
<blockquote>
<p>In order to protect the data in the mmap’d file, modifications are not allowed. To modify mmap’d data, it is necessary to create a copy-on-write (COW) version of the data. This is done by calling <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code>. Once called, the old version can be discarded, and modifications to the new version will affect the file from which the mmap object was created.</p>
</blockquote>
So, you have to call <code>m.
