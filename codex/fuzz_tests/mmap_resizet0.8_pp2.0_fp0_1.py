import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

a
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: mmap can't extend memory maps past their original size
</code>

