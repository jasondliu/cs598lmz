import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I thought that the mmap object would be updated when the file is truncated, but it seems not.
Is there a way to update the mmap object when the file is truncated?


A:

I think you are looking for <code>mmap.resize</code>:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
...
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     m.resize(0)
...     a = m[:]
...
&gt;&
