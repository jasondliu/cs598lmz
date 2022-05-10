import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "C:/Users/Mariusz/PycharmProjects/untitled/Test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I have no idea how to fix this. If I leave the <code>f.truncate()</code> line out, I get a <code>mmap.error</code>.
I'd really appreciate any help.


A:

Use <code>mmap.resize</code> instead.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mmap.resize(m, 0)
    a = m[:]
    print(a)
</code>

