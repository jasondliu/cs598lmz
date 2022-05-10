import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print (a)
</code>
Output is:
<code>
Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print (a)
ValueError: read-only access to 0x7f8e8e1dfac0
</code>
Is that a bug? Or I'm doing something wrong?


A:

Try the following:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    print(m.read())
</code>
This works on both a Mac and a Linux machine. The problem is that you are trying to read from the mmap object rather than from the file.

