import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws exception:
<code>Traceback (most recent call last):
  File "C:\Users\alex\test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
But if I change line:
<code>f.truncate()
</code>
to:
<code>f.write(bytes(1))
</code>
exception doesn't throw.
Why?


A:

<code>f.truncate()</code> will truncate the file to the current position of the file pointer. <code>f.write(bytes(1))</code> will write one byte to the file, and advance the file pointer by one byte.
So, after <code>m = mmap.mmap(f.fileno(), 0)</code>, the file pointer is at the end of the file, so <code>f.truncate()</code> truncates the file to size 0.
However, after <code>f.write(bytes(1))
