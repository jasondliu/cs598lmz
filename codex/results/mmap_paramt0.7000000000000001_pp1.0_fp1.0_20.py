import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    m[0] = b'b'
    print(f.read())
</code>
(I'm using Python 3, but the same applies to Python 2.)
The output is <code>b</code>, so the memory-mapped data was written to the file. However, I can also see that the file's size is now 2 bytes, which is strange, because I thought I'd just written a single byte to the file.
I can also see that this happens in the Python 2 shell:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; f = open('test', 'wb')
&gt;&gt;&gt; f.write('a')
&gt;&gt;&gt; f.close()
&gt;&gt;&gt; f = open('test', 'r+b')
&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
&gt;&gt;&gt; m
