import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But it doesn't work.
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there any way to truncate a file that is mmapped in Python?


A:

You can't do that. The mmap object is a view of the file at the time it was opened.
If you want to truncate the file you must close the mmap object first.

