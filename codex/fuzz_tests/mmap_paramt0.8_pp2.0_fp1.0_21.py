import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: cannot mmap an empty file
</code>
I suspect I'm just missing something obvious.
Note: I'm using Python 3.3.


A:

According to <code>mmap.mmap(fileno, length)</code> docs:
<blockquote>
<p>length is the number of bytes to map.</p>
</blockquote>
So, your <code>mmap</code> call should be:
<code>m = mmap.mmap(f.fileno(), 1)
</code>
Which mapps <code>1</code> byte at the beginning of the file.

