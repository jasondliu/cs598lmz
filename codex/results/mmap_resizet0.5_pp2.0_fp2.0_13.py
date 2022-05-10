import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The result is <code>b'\x00'</code>, which is not what I expected.
I know that I can use <code>mmap.resize</code> to do that, but I am curious why this happened.


A:

You open the file in write mode, which truncates the file.
The <code>mmap</code> object is now pointing to an invalid memory location, as the file is empty.
You can't read from the <code>mmap</code> object anymore, but it is still possible to write to it.
If you want to truncate the file, you need to resize the <code>mmap</code> object first:
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
...
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.resize(0)
...     f.
