import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't find any documentation on this.  Is this a bug?  Is there a way to get the data from the mmap object?


A:

I think you're misunderstanding what the <code>mmap</code> object is. It's not a copy of the file, it's a view into the file. If you truncate the file, the view is no longer valid.
If you want to truncate the file and keep the data, you can use <code>m.resize</code> to resize the file and then <code>m.move</code> to move the data to the beginning of the file.

