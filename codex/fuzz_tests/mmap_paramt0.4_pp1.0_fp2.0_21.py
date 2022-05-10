import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
I was expecting that the file would now contain the byte <code>2</code>, but it still contains the byte <code>1</code>.  What am I doing wrong?


A:

You need to <code>flush</code> the memory map:
<code>m.write(bytes(2))
m.flush()
</code>
The documentation for <code>mmap.flush</code> says:
<blockquote>
<p>Write changes made to the memory-mapped file back to the original file.</p>
</blockquote>

