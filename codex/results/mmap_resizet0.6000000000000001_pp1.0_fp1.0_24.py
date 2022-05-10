import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory mapping closed or invalid
</code>
I guess that the mapping is closed when I truncate the file, but why? Is there a way to keep the mapping opened ?


A:

According to the documentation:
<blockquote>
<p>The file size cannot be changed while the memory map is active.</p>
</blockquote>
Thus, you should truncate after closing the memory map.

