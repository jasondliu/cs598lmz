import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The file is opened in <code>r+b</code> mode, so I expect the mmap to be readable. However, I get the following error:
<code>Traceback (most recent call last):
  File "/home/user/workspace/test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: mmap can't extend file to larger size
</code>
If I open the file in <code>rb</code> mode instead, the error is gone. I'm using Python 3.5.
Why does this happen? Is this a bug?


A:

You can't have a <code>mmap</code> with a file size of 0.
<code>mmap.mmap(f.fileno(), 0)</code> maps the whole file.
<code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)</code> maps the whole file, but only for reading.

