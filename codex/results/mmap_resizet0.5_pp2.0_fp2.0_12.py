import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect that the <code>a</code> variable will be an empty byte array, but I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why is that?


A:

The problem is that you are truncating the file after you create the mmap.
The mmap object is basically a memory mapping of the file.  So, when you truncate the file, it is still mapped to the original size.  This is why you get the error.
Move the <code>f.truncate()</code> call up before the <code>m = mmap.mmap(f.fileno(), 0)</code> call, and it will work.

