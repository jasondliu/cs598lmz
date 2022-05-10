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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
How can I read from a mmap object after truncating the file?


A:

The documentation for <code>mmap</code> states that:
<blockquote>
<p>The optional size argument, if given, specifies the initial size of the array. The optional flags argument has the same meaning as the flags parameter of the built-in open() function.</p>
</blockquote>
So you can use a <code>size</code> argument when creating the mmap to specify the size of memory you want to map.
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f
