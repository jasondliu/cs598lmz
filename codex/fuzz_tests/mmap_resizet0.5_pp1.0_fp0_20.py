import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises the following exception:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I'm using Python 3.5.2 on Windows 7.
I can't understand why it happens. The file is not empty. It contains one byte.


A:

The file is empty because you truncated it.  The <code>mmap</code> object is still pointing to the old file size.  You need to close the <code>mmap</code> object, then reopen it with the new size.

