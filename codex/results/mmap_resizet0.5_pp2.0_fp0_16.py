import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is:
<code>b'\x01'
</code>
That means, the data is still there.
But if I remove the <code>f.truncate()</code> line, the data is gone.
So, is there any way to flush the mmap cache?
I have tried <code>m.flush()</code> and <code>m.sync()</code> but both doesn't work.


A:

<code>truncate</code> doesn't immediately change the file size, it only changes the size the next time you write to the file. So the <code>mmap</code> is still valid at the time you read it.
From the <code>mmap</code> docs:
<blockquote>
<p>A <code>&lt;code&gt;mmap&lt;/code&gt;</code> object also provides new-style file object methods, such as <code>&lt;code&gt;fileno()&lt;/code&gt;</code> and <code>&lt;code
