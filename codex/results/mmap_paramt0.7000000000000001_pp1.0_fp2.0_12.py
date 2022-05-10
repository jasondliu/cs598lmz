import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)

with open('test', 'r') as f:
    print(list(f))
</code>
This yields the following output:
<code>['']
</code>
The second (resized) byte is not read.
How can I read a file that has been resized, without closing the file and re-opening it?
(I am using Python 3.4.3 on Windows 7, but I am interested in answers for all platforms.)


A:

You can use <code>mmap.resize</code>.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(list(m))
</code>

