import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It returns
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 4, in &lt;module&gt;
ValueError: mmap length is greater than file size
</code>
Is it a bug ? I expected a <code>bytes</code> or <code>None</code>.


A:

Yes it's a bug, as @user2357112 pointed out.
As per the documentation on the <code>mmap</code>, "The mmap constructor creates a memory-mapped file. An empty string is returned on error."
Your code should not raise an exception.
<blockquote>
<pre><code>&lt;code&gt;&amp;gt;&amp;gt;&amp;gt; import mmap
&amp;gt;&amp;gt;&amp;gt; f = open('01.txt', 'r+')
&amp;gt;&amp;gt;&amp;gt; mm = mmap.mmap(f.fileno(), 0)
&amp;gt;&amp;gt;
