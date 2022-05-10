import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.truncate(8)
    b = m[:]

assert a == b
</code>
Output:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 11, in &lt;module&gt;
    b = m[:]
ValueError: mmap offset is beyond the end of the file
</code>


A:

From the docs:
<blockquote>
<p>The memory mapped file cannot be resized in place. If the file is resized, <code>&lt;code&gt;mmap&lt;/code&gt;</code> objects will raise an exception on attempts to read or write beyond the current end-of-file.</p>
<p>One way to overcome this limitation is to unmap the file with <code>&lt;code&gt;close()&lt;/code&gt;</code> and create a new <code>&lt;code&gt;mmap&lt;/code&gt;</code> object with the new size.</p>
</blockquote>
So change the
