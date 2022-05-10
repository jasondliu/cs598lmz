import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm using Python 3.7.3.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> argument set to <code>0</code>.
The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>If length is omitted or 0, the maximum length of the map will be the current size of the file when mmap is called.</p>
</blockquote>
So, when you call <code>mmap.mmap</code> with <code>length=0</code>, it will create a map of length 1, since the file is 1 byte long.
Then, when you truncate the file, the map is still 1 byte
