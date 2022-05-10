import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
Output:
<code>&gt;&gt;&gt; b''
</code>
How can I get the file's contents without expanding the file size? 


A:

You can't. The file is truncated, so there is no data to read.
From the docs:
<blockquote>
<p>If length is not specified, or is larger than the current file size, the file is extended to contain length bytes. <strong>If length is specified and is smaller than the current file size, the file is truncated.</strong></p>
</blockquote>

