import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print a
    m.resize(0)
    m.close()

with open('test', 'wb') as f:
    f.write(bytes(2))
</code>
I expected m.resize to create and truncate the file, but instead got this error:
<code>Traceback (most recent call last):
  File "main.py", line 14, in &lt;module&gt;
    m.resize(0)
ValueError: resize() must be 0 or &gt;= size()
</code>
Is there way to resize the mmap object, the way the file was before opening the mmap object successfully?


A:

After the file is truncated, the old file contents are still available through the mmap object.
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m
