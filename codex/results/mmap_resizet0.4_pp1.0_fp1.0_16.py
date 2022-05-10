import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't find anything in the docs about this.
I found this question on SO, but it's about truncating a file which is already mmapped.


A:

From the docs:
<blockquote>
<p>The file size cannot be changed, but may be extended. To change the file size, use <code>&lt;code&gt;os.truncate()&lt;/code&gt;</code> on the underlying file first.</p>
</blockquote>

