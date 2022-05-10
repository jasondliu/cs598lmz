import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code> which is not what I expected.
I expected it to be an empty byte array.
Why is this?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function creates a new memory map. The <em>fileno</em> argument is the file descriptor of the file to be mapped. The optional <em>length</em> argument specifies the length of the mapping (in bytes). If <em>length</em> is omitted, the entire file is mapped.</p>
</blockquote>
So, you are mapping the entire file, which is still 1 byte long.

