import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Output:
<code>Traceback (most recent call last):
  File "m.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
How can I make this work?

