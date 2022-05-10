import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)

with open('test', 'rb') as f:
    print(f.read(1))
</code>
I'm using Python 3 (tested both with Python 3.4 and Python 3.5). 
The output is <code>b'\x01'</code> instead of <code>b'\x02'</code>. Why is this the case?


A:

<code>mmap.mmap</code> doesn't support writing at the moment (but it probably should). However, it can do writes on <code>mmap.ACCESS_WRITE</code> objects.
From the documentation:
<blockquote>
<p><code>&lt;code&gt;mmap.ACCESS_WRITE&lt;/code&gt;</code></p>
<p>Allows writing to the buffer. The buffer must be private.</p>
</blockquote>
The private buffer, in this case, corresponds to the <code>mmap.mmap</code> object.
The documentation says:
<blockquote>
<p>[...]
