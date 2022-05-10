import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 48
    print(m[0])
</code>
I would expect the output to be:
<code>1
0
</code>
However, the actual output is:
<code>1
1
</code>
This is the behaviour I would expect if I had opened the file in read-only mode, but as you can see, I opened it in read-write mode.
I am using Python 3.6.3 on Windows 7.
What am I missing here?


A:

You can't use <code>mmap</code> on an empty file. 
<code>mmap.mmap</code> docstring:
<blockquote>
<p>Create a new memory-mapped file object. The size argument specifies the initial size of the file. The optional access argument specifies the access mode, and defaults to ACCESS_WRITE.</p>
</blockquote>
And:
<blockquote>
<p>If the file is opened for read-only access, this method raises <code>&lt;code&gt;Environment
