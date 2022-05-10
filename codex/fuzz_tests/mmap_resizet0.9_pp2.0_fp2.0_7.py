import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
After truncate the file, I want to read previous content of the file. In this scenario, I want to get <code>[1]</code> in <code>a</code>, but it gives error
<blockquote>
<p>ValueError: cannot resize mmap - size changed since last mmap().</p>
</blockquote>
I also tried <code>m.resize(0)</code> or <code>m.close()</code> then reopen the file, but didn't work.


A:

Have you tried the <code>mmap.resize</code> method?
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>

