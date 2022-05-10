import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.flush()
    print(m[0])

with open('test', 'r+b') as f:
    print(f.read(1))
</code>
The output of this script is <code>2</code> then <code>1</code>. Why is that?
When I remove the <code>f.seek(0)</code> statement, the output is <code>2</code> then <code>2</code> (as expected).
I use python 3.7.3 on Windows 10.


A:

On Windows, files opened in <code>os.O_RDWR</code> mode aren't opened in write-through mode by default. The default behavior is to open files in write-through mode only if <code>FILE_FLAG_WRITE_THROUGH</code> is specified as a flag. The <code>io</code> module doesn't give you access to this flag, so the <code>open</code> function can't change the default behavior.
The exact behavior of the <code>mmap</code> module
