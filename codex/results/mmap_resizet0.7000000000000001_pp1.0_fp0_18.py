import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<blockquote>
<pre><code>&lt;code&gt;Traceback (most recent call last):
  File "mmap_test.py", line 8, in &amp;lt;module&amp;gt;
    a = m[:]
ValueError: mmap offset is greater than file size
&lt;/code&gt;</code></pre>
</blockquote>
To fix the problem, we can unmap the file before truncating:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>
Output:
<blockquote>
<pre><code>&lt;code&gt;b''
&lt
