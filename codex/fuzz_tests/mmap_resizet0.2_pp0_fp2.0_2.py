import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would like to know why this happens.
I know that I can use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but I would like to know why the latter doesn't work.

