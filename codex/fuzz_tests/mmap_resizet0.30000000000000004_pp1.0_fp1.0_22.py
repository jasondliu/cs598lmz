import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I understand that the file is empty, but I want to read the data that was in the file before truncation. Is there a way to do this?


A:

You can't.
The data is gone.
If you want to keep it, you have to copy it somewhere else before truncating the file.

