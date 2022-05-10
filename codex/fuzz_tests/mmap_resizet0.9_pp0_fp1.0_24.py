import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Will raise
<code>Traceback (most recent call last):
  File "truncatetest.py", line 9, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
Updating the <code>mmap</code> size to <code>0</code> succeeds but isn't quite what I want to achieve. And I must admit I don't quite follow the <code>mmap</code> docs in this case.


A:

<blockquote>
<p>As far as I understand it, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is not a file itself. So
  truncating the file should be ok, right?</p>
</blockquote>
Precisely. You're making a mmap of a file, and you're not changing the size or shape of the mmap at all. You're just doing something to a file which the mmap has nothing to do with.
