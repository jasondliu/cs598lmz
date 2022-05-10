import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am aware that I can use <code>m.resize(0)</code> to fix this, but I am wondering why the <code>truncate</code> call doesn't work.


A:

From the docs:
<blockquote>
<p>The file’s current size is reported by the <code>&lt;code&gt;st_size&lt;/code&gt;</code> attribute of the <code>&lt;code&gt;stat_result&lt;/code&gt;</code> structure returned by <code>&lt;code&gt;os.fstat()&lt;/code&gt;</code>.</p>
</blockquote>
<code>mmap</code> does not know about the <code>truncate</code> call, because it does
