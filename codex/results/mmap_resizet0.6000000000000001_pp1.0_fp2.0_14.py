import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(len(a))
</code>
I expected <code>a</code> to be an empty byte-string, but it appears to contain the single byte <code>0</code>. Why? Is there a way to make this example return an empty byte-string?


A:

This is a bug in Python 3.3, which was fixed in 3.4.
From the 3.3 documentation:
<blockquote>
<p>The data attribute is a read-only <code>&lt;code&gt;bytes&lt;/code&gt;</code> object that contains the contents of the mapped file. The data is not cached in memory.</p>
</blockquote>
In other words, the <code>data</code> attribute is a view into the file.
From the 3.4 documentation:
<blockquote>
<p>The data attribute is a <code>&lt;code&gt;bytes&lt;/code&gt;</code> object containing the data from the file. The data is cached in memory.</p>
</blockquote>
In other words, the <code>data</code
