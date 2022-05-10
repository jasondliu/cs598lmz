import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm using Python 3.6.1.


A:

You are trying to access the file after it has been truncated.
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
... 
&gt;&gt;&gt; a = m[:]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
ValueError: mmap cannot extend file
</code>

