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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I was expecting the mmap to be updated with the new file size.
Is there a way to update the mmap with the new file size?


A:

You can't do that. The mmap is a view into the file, and it can't be updated to reflect changes in the file.
You can use <code>mmap.resize</code> to change the size of the mmap, but that will truncate the file to the size of the mmap.

