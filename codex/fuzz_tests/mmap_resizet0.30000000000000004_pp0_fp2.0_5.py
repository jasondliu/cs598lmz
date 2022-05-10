import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect to get an empty byte array, but it gives me an error:
<code>Traceback (most recent call last):
  File "mmap.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I get an empty byte array?


A:

You can't.
The <code>mmap</code> object is a view of the file, and once you truncate the file, the view is no longer valid.
You could create a new <code>mmap</code> object, but that would be a view of the new, empty file.

