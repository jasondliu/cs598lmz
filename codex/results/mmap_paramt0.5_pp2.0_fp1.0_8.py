import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
This is a simplified example, but it's enough to show the issue.
When I try to write to the <code>mmap</code>, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.write(bytes(2))
ValueError: mmap can't modify a readonly or copy-on-write memory map
</code>
How do I make an <code>mmap</code> object writable?


A:

The first argument to <code>mmap</code> is the file descriptor. The second argument is the length of the map.
<code>m = mmap.mmap(f.fileno(), 1)
</code>

