import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
When I run this, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
I would expect the mmap to be invalidated when the file is truncated, but it seems that it is not.
I know I can work around this by using <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but I would like to know why this happens.
I am using Python 3.5.2 on Ubuntu 16.04.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The <em>length</em> argument specifies the number of bytes to map. The entire file is mapped if <em>length</em> is omitted or is larger than the file’s current size.</p>
</blockquote>
So, when you trunc
