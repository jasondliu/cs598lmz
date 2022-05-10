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
This prints <code>b'\x00'</code>, but I would expect it to print <code>b'\x01'</code>.
I'm using Python 3.6.1 on Windows 10.


A:

The documentation says:
<blockquote>
<p>The file must be opened in <code>&lt;code&gt;r+b&lt;/code&gt;</code> mode. This is because Windows does not permit one process to extend the size of a file mapped by another process.</p>
</blockquote>
So you can't truncate the file when it is mapped.

