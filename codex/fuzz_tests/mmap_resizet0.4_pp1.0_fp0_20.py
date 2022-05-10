import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The error is:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
But if I don't use <code>m[:]</code>, it will be OK.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    print(m[:])
</code>
The output is:
<code>b'\x00'
</code>
I want to know why it happens.


A:

In the first example, you are calling <code>m[:]</code> before truncating the file, so the file size is still 1.  The second example calls <code>m[:]</code> after truncating the file, so the file
