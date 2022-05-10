import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
The error is:
<code>&gt;&gt;&gt; Traceback (most recent call last):
  File "&lt;stdin&gt;", line 7, in &lt;module&gt;
ValueError: mmap offset is greater than file size
</code>
Now, I can’t explain this error.
According to the documentation, the <code>mmap</code> object is supposed to raise a <code>ValueError</code> if <code>length == 0</code>. But that is clearly not what’s happening here.
What is going on?


A:

The file you created above used to be 1 byte long, now it doesn't exist anymore. 
According to the docs:
<blockquote>
<p>The size argument specifies the initial size of the mapping (in bytes). If <code>&lt;code&gt;size&lt;/code&gt;</code> is larger than the current size of the underlying file, the file is grown to contain <code>&lt;code&gt;
