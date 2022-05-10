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
Why is this? I thought that the <code>mmap</code> object would be aware of the file size change.


A:

The <code>mmap</code> object is not aware of the file size change.
The <code>mmap</code> object is a view of the file at the time it was created.
The <code>mmap</code> object is not a view of the file at the time it is used.

