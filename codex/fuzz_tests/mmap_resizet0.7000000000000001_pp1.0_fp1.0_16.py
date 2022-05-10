import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am getting this exception:
<code>Traceback (most recent call last):
  File "C:\Users\Me\Desktop\test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why is this happening? How can I fix it?


A:

The answer is in the error. <code>mmap</code> is a memory map of a file. If you truncate the file to a smaller size, the file will still be that size, but the <code>mmap</code> will still be the size of the original file.

