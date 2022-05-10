import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.6.1 on Windows 10.
I am aware that I can use <code>m.resize()</code> to resize the mmap object, but I would like to know why the above code does not work.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
The <code>mmap</code> object is not updated when you truncate the file.
You can see this by printing the <code>mmap</code> object:
<code>print(m)
</code>
Output:
<code>&lt;mmap.mmap object at 0x7f8f9d6a4f80&gt;
</code>
You can see that the <code>mmap</code> object is still pointing to
