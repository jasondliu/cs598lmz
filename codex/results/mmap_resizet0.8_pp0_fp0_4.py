import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.truncate()
    m.resize(0)
    b = m[:]
    m.close()


print(a)
print(b)
</code>
In both cases <code>a</code> and <code>b</code> are empty bytes, but my understanding is that the code should always raise an exception, since the file is truncated to zero length before the memory is accessed.
I'm using Python 3.4.4 on Windows.


A:

Notes:

Since you want to truncate the file, there is no need to use <code>mmap.mmap</code>, because it also maps the whole file (and also due to the fact that you only want to truncate a file containing 1 byte).
To truncate a file in Python you can use <code>f.truncate(0)</code>.
Since you are truncating the file after mapping the file with <code>mmap</code>, you should use <code>mmap.ACCESS_WRITE</code> in the flags argument of <code>mmap.mmap</code>


Here is a working
