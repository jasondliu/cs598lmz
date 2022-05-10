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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.6.5 on Windows 10.
I am trying to understand why this is happening. I am aware that I can use <code>m.seek(0)</code> to fix this, but I am curious why this is happening.
I am also aware that I can use <code>m.resize(0)</code> to fix this, but I am curious why this is happening.
I am also aware that I can use <code>m.close()</code> to fix this, but I am curious why this is happening.
I am also aware that I can use <code>m.flush()</code> to fix this, but I am curious why this is happening.
I am also aware that I can use <code>m.seek(0)</code> and <code>m.resize(0
