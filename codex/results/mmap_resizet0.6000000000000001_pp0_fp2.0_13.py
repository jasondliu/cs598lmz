import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 8, in &lt;module&gt;
IndexError: string index out of range
</code>
I would expect the <code>a = m[:]</code> line to raise an <code>mmap.error</code> exception:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    try:
        a = m[:]
    except mmap.error:
        print('ok')
</code>
<code>ok
</code>
But if I reopen the file and call <code>mmap.mmap</code> again, everything is fine:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    try:
        a = m[:]
    except mmap.error:
        print
