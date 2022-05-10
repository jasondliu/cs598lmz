import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
But I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I know that <code>truncate()</code> will truncate the file to the current position of the file pointer, but why is it that the file pointer isn't at the end of the file?


A:

The file pointer is at the end of the file.  The problem is that <code>mmap()</code> wants the length of the file in bytes.  If the file is empty, you should pass <code>0</code> for the length.

