import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Is there a way to do this without closing the file?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length will be used (when <em>access</em> is <code>&lt;code&gt;mmap.ACCESS_WRITE&lt;/code&gt;</code> or <code>&lt;code&gt;mmap.ACCESS_COPY&lt;/code&gt;</code>, the file must be seekable and have a <code>&lt;code&gt;fileno()&lt;/code&gt;</code>).</p
