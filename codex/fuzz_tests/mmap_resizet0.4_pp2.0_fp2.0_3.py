import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Why? How can I get the contents of the file?


A:

The <code>mmap</code> object is tied to the size of the file. When you truncate it, the <code>mmap</code> object is no longer valid.
You could try to <code>mmap</code> the file again, but you'd have to close the file first.

