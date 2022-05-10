import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(len(a))
</code>
Using <code>ctypes.memmove</code> gives the same error:
<code>In [19]: ctypes.memmove(id(a), id(m[:]), len(m[:]))
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
&lt;ipython-input-19-8855afb1a2e3&gt; in &lt;module&gt;()
----&gt; 1 ctypes.memmove(id(a), id(m[:]), len(m[:]))

OSError: [Errno 22] Invalid argument
</code>
This seems to be a Python issue, mostly due to the following documentation,
<code>Addresses returned from Python have no special alignment requirements, and may not be suitable for direct use with the platform 'C' library.</code>
However, this answer suggests Python3 fixed this issue.
Anybody managed to find a workaround for this?


A:

This is definitely a python 3.6 C python bug.
Your code works fine in python 3.4 and python 3
