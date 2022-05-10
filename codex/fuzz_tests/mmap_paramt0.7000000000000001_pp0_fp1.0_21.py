import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
</code>
However, I get a <code>ValueError</code> when I try to resize the file to a larger size.
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(10)
ValueError: Cannot resize a mmap to a larger size.
</code>
I don't understand why I can't do this. Is there a way to resize the file to a larger size?

