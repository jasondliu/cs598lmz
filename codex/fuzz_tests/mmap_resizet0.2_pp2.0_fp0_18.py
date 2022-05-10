import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I truncate the file while keeping the mmap object?


A:

You can't. The mmap object is tied to the file size, and the file size is tied to the mmap object.
You can close the mmap object, truncate the file, and then re-open the mmap object.

