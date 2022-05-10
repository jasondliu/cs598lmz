import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
It raises <code>ValueError: mmap offset is greater than file size</code> exception.
I know that I can use <code>mmap.resize</code> method, but I want to know why this exception is raised.
I've read the source code of <code>mmap</code> module, but I didn't understand why this exception is raised.
I've also read this question, but it doesn't answer my question.

