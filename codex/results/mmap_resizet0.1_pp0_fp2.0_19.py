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
I am using Python 3.6.1 on Windows 10.
I have tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but I get the same error.
I have also tried to use <code>m.seek(0)</code> before <code>a = m[:]</code>, but I get the same error.
I have also tried to use <code>m.seek(0)</code> before <code>f.truncate()</code>, but I get the same error.
I have also tried to use <code>m.seek(0)</code> before <code>m.resize(0)</code>, but I get the same error.
I have also tried to use <code>m.seek(0)</code>
