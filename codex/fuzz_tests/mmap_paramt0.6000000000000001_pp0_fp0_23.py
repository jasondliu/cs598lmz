import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(2)
    m.flush()
    m.close()
</code>
This still produces an error.


A:

The problem is that the <code>mmap</code> object doesn't close the file. So you can't write to the file in the same process.
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
1
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m[0:1] = bytes(2)
...     m.flush()
...     m.close()
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     f.write(bytes(3))
... 
Traceback (most recent call last):
  File "&lt;
