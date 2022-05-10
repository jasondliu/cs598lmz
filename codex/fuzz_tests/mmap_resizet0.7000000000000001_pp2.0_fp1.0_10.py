import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)

print(len(a))
&lt;/code&gt;</code></pre>
</blockquote>
In this example, <code>a</code> is <code>b'\x00'</code>. 
According to the documentation, the <code>mmap</code> object should be invalidated. Shouldn't <code>a</code> be an empty byte array?


A:

As per the documentation of <code>mmap.mmap</code>:
<blockquote>
<p><em>When the <code>&lt;code&gt;mmap_object&lt;/code&gt;</code> is garbage collected</em>, <em>the <code>&lt;code&gt;underlying file is closed</em></em> (if <em>you want to continue using the file, you must close it explicitly</em>)</p>
</blockquote>
So, the <code>m</code> object is invalidated at the end of the <code>with</code> block, but the file is still open.

