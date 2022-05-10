import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the file to be empty, but the output of <code>a</code> is:
<code>b'\x00'
</code>
Why is that?


A:

The file is empty, but there is still some data in the mmap object. This happens because the <code>mmap</code> object caches the data that you read from it. If you want to release the cached data, you can call <code>mmap.resize</code> with a size of 0:
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     a = m[:]
... 
&gt;&gt;&gt; a
b''
&gt;&gt;&gt; m.resize(0)
&gt;&gt;
