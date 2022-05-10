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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> object to be updated when the file is truncated.
Is there a way to make this work?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is updated when the file is resized.
<code>f.truncate()</code> does not resize the file.
<code>f.truncate(0)</code> resizes the file.

