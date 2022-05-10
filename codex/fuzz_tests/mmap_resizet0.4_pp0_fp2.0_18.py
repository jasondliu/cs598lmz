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
  File "C:/Users/User/PycharmProjects/untitled/main.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I fix it?


A:

<code>mmap</code> is not a general-purpose file object. It is a view of a file, and if you truncate the file, the view is no longer valid.
If you want to truncate a file, you need to do it before you create the <code>mmap</code> object:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

