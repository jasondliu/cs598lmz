import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
I get this error:
<code>Traceback (most recent call last):
  File "mmap.py", line 8, in &lt;module&gt;
    m[0] = 0
ValueError: mmap: invalid argument
</code>


A:

According to the python documentation on <code>mmap</code>, you have to pass a certain length to the constructor:
<blockquote>
<p>The <em>length</em> argument specifies the length of the mapping (in bytes).
  If <em>length</em> is omitted, the <code>&lt;code&gt;length&lt;/code&gt;</code> of the file is used.</p>
</blockquote>
So in your case, you could simply use:
<code>m = mmap.mmap(f.fileno(), 1)
</code>

