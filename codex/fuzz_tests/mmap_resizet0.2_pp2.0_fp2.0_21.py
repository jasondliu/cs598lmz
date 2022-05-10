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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.4.3.


A:

The problem is that you are using <code>mmap.mmap</code> with a length of 0.
<code>mmap.mmap(f.fileno(), 0)
</code>
This means that the mmap object is not actually mapped to any memory.  The documentation states:
<blockquote>
<p>If length is 0, the maximum length of the map is the current size of the file when mmap is called.</p>
</blockquote>
Since the file is empty when you call <code>mmap</code>, the maximum length of the map is 0.  This means that the map is not actually mapped to any memory.  When you try to access the map, you get the error you see.
If you want to map the entire file, you
