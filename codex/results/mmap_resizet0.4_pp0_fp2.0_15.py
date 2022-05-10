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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
If I comment out the <code>f.truncate()</code> line, it works fine.
What is the reason for this?


A:

The <code>mmap</code> module uses the current file size to determine the size of the mapping.
When you truncate the file, the <code>mmap</code> module is no longer valid.
The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The mmap object can be used anywhere an object is expected which supports the <code>&lt;code&gt;buffer&lt;/code&gt;</code> protocol.</p>
</blockquote>
The <code>buffer</code> protocol is deprecated, but the <code>memoryview</code> type still supports it:
