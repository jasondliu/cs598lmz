import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(type(m))
</code>
In this case I get a <code>mmap.error</code> with the error message: <code>mmap can't open file: No such file or directory</code>. I know it cannot open it because Python is holding that file open and it is not available to mmap. If I use <code>sys.getrefcount(f)</code>, I see that it is 2. I've also looked at the mmap source code and I can see that it is trying to open the file.
Is there a way to open a writable mmap on a file in Python 2?


A:

First, you need to close the file object. Then, you can open it again with <code>os.open</code>, which will return a file descriptor that can be passed to <code>mmap.mmap</code>.
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:

