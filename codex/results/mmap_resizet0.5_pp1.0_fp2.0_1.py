import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line <code>a = m[:]</code> raises a <code>ValueError: mmap offset is greater than file size</code>.
If I change the last line to <code>a = m[:1]</code> or <code>a = m[0]</code>, it works as expected.
Why is that?


A:

From the documentation of <code>mmap.mmap</code>:
<blockquote>
<p>If <em>length</em> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map will be the current size of the file when <em>mmap</em> is called.</p>
</blockquote>
So you are mapping the entire file, which is 1 byte long. Later, you truncate the file to 0 bytes. Now the map is invalid, because its size is greater than the file's size.

