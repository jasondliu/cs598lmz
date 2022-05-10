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
I would expect that <code>m[:]</code> would return <code>b''</code> since the file is empty.
Is there a way to get the contents of the file after truncating it?


A:

<code>mmap</code> is a view of the file, not a copy of the file. When you truncate the file, the <code>mmap</code> is no longer valid.
<code>mmap</code> is a view of the file, not a copy of the file. When you truncate the file, the <code>mmap</code> is no longer valid.

