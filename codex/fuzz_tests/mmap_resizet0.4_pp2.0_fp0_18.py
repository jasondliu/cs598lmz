import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to get <code>a</code> to be an empty <code>bytes</code> object, but instead I get a <code>ValueError</code> exception.
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Is there a way to do this?


A:

From the docs:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map will be the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called.</p>
</blockquote>
So, you can just omit the length argument:
<code>m = mmap.mmap(f.fileno(), 0)
</code>

