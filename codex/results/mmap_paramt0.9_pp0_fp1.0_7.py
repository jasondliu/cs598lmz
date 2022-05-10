import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.write(bytes(2))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m.read())  # b'\x02\x02'
</code>
From the mmap documentation https://docs.python.org/2/library/mmap.html
<blockquote>
<p>The format of the mmap call is:<br/><br/>
<code>&lt;code&gt;mmap.mmap (fileno, length[, flags [, prot [, access [, offset]]]])&lt;/code&gt;</code></p>
<p>[...]</p>
<p><code>&lt;code&gt;fileno&lt;/code&gt;</code> is the integer file descriptor of the file to be mapped.</p>
<p>[...]</p>
<p><code>
