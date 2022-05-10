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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the mmap is still pointing to the old file size, but I don't know how to fix it.
I tried calling <code>m.resize(0)</code> and <code>m.resize(1)</code> but it didn't help.
I also tried calling <code>m.close()</code> and then reopening the file, but I get the same error.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
You can fix this by calling <code>m.resize(0)</code> and then <code>m.resize(1)</code>.

