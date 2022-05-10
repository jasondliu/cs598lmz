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
ValueError: mmap length is zero
</code>
I'm not sure why this is happening. I'm on Windows 10.


A:

The problem is that you're truncating the file before you read from the mmap.  The mmap is still pointing to the old file size, which is now zero.  You can fix this by moving the <code>f.truncate()</code> to after the <code>m[:]</code> line.

