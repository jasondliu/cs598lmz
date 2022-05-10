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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I am using Python 3.6.5 on Windows 10.
I am aware that I can use <code>mmap.resize</code> to resize the file, but I would like to know why this error is occurring.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The <em>length</em> argument specifies the initial size of the mapped region. If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
