import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap can't extend file to larger than 2GB on 32-bit system
</code>
I am using Python 3.6.3.
What am I doing wrong?


A:

The problem is that <code>mmap</code> is trying to map the whole file, but there is no file (it was truncated).
As a workaround you can create a new file of the same size and map it.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    size = f.seek(0, 2)
    f.truncate()
    with open('test', 'r+b') as f:
        f.truncate(size)
        m = mmap.
