import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
But if I change the line <code>f.truncate()</code> to <code>f.truncate(0)</code>, then the code works.
Why does it work with <code>f.truncate(0)</code> and not with <code>f.truncate()</code>?

