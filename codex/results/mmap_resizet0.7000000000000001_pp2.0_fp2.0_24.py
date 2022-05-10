import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And I get <code>IndexError: index out of range</code> on the last line.  If I were to attempt to read the same size or less than what I wrote, it would work fine.  However, I know for a fact that I'm already reading the whole file, because if I do:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
    f.truncate()
    a = m[:]
</code>
I get <code>1</code> as the result of <code>m.size()</code>.  Why am I getting this error and how can I fix it?


A:

You should use <code>os.truncate</code> for the file truncation.
From the docs:
<blockquote>
<p>This operation may be implemented via a call to ftruncate; many
  systems can optimize truncation to avoid some disk operations.</p>
</blockquote>
<code>import os
...
with open
