import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws a <code>ValueError: mmap offset is greater than file size</code> exception.
I am using Python 3.6.1 on Windows 10.
I have tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but it didn't help.
I have also tried to use <code>m.resize(0)</code> after <code>f.truncate()</code>, but it didn't help either.
I have also tried to use <code>m.close()</code> after <code>f.truncate()</code>, but it didn't help.
I have also tried to use <code>m.close()</code> after <code>m.resize(0)</code>, but it didn't help.
I have also tried to use <code>m.close()</code> after <code>f.truncate()</code> and <code>m.resize(0)</code>, but it didn't help.
I have also tried to use <code>m.seek(0)</
