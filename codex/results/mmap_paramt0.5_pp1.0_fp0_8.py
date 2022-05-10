import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1024)
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m.resize(1024)
ValueError: negative size argument to resize()
</code>
What does that error mean and how can I fix it?


A:

If you are on Windows, then <code>mmap</code> does not support resizing.  The documentation says:
<blockquote>
<p>On Windows, if length is 0, the map can’t be resized, so ValueError is raised.</p>
</blockquote>

