import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I don't understand why I get this error. I think that the length of the file is zero, but the length of the mmap is not zero.
What am I doing wrong?


A:

The <code>mmap</code> object is not updated when you truncate the file.
You can call <code>mmap.resize()</code> to change the size of the mmap object.

