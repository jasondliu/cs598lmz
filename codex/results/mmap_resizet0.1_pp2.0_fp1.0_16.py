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
ValueError: mmap offset is greater than file size
</code>
I don't understand why this is happening. I thought that the mmap object would be updated when the file is truncated.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>m[:]</code> to get the contents of the file. This is equivalent to <code>m[0:]</code> which means "get the contents of the file starting at offset 0".
Since you truncated the file, the offset 0 is now beyond the end of the file, so you get the error.
If you want to get the contents of the file, you should use <code>m[:m.size()]</code> instead.

