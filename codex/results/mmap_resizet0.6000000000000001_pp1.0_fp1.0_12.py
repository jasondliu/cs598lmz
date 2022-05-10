import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # This will raise an exception in python 2, but not in python 3.
</code>
In python 2, this raises an exception:
<code>mmap.error: cannot find length of file
</code>
In python 3, this does not raise an exception.
Is there a way to make python 3 raise an exception in this case?


A:

I think this is a bug, but I'm not sure.
I've tried to reproduce it in Python 2 and Python 3.4, and I've failed.
However, in Python 3.5, I can reproduce it.
To fix it, I think you can do this:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>
The <code>access</code> parameter is the default value in Python 3.5, but not in Python 3.4. This seems to fix the problem.

