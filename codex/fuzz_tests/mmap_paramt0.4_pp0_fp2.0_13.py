import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = 0
    print(m)
    m[0] = 1
    print(m)
    m.flush()
    print(m)
</code>
The output is:
<code>&lt;mmap.mmap object at 0x7f0f8d7f4b70&gt;
&lt;mmap.mmap object at 0x7f0f8d7f4b70&gt;
&lt;mmap.mmap object at 0x7f0f8d7f4b70&gt;
&lt;mmap.mmap object at 0x7f0f8d7f4b70&gt;
</code>
I expected that the last print statement would print <code>&lt;mmap.mmap object at 0x7f0f8d7f4b70&gt;</code> only if the file was not flushed.
What am I missing here?


A:

You're not missing anything.  The <code>flush()</code> method is a no-
