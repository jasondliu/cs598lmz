import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object would be updated when the file is truncated, but it seems that it is not.
Is there a way to update the mmap object after the file has been truncated?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is updated when the file is resized.
<code>truncate</code> does not resize the file, it just makes the file shorter.
<code>resize</code> does resize the file, it can make the file shorter or longer.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:

