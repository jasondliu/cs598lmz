import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line produces <code>ValueError: cannot mmap an empty file</code>. 
I'm aware that I can use <code>m.close()</code> and open the file again to get the updated data, but I would like to avoid the extra read operation.
Is there a way to resize a file while keeping the mmap object valid?


A:

As of Python 3.3, the answer is: no, there is no way to resize a file while keeping the mmap object valid.
In Python 3.4, you'll be able to use <code>mmap.resize</code> to resize a file and keep the mmap object valid.

