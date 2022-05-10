import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m[0] = 2
    print(m)
    print(len(m))
    print(len(a))
</code>
It outputs:
<code>2
255
0
</code>
It was expected to output <code>0</code> at the last line. This code tries to store the content of <code>a</code> (bytes taken from <code>m</code>) and then tries to set the first byte to <code>2</code>. Shouldn't these previous operations raise errors?
Is this an implementation detail, since it occured both in cpython and pypy?

