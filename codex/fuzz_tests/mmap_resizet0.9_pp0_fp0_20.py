import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me a OSError: [Errno 28] No space left on device.
The reason is, the <code>flock</code> on line 6 does not get released until line 11, so line 8 actually has no effect. Renaming the file will release the flock.
This is the same problem with apps that use the mmap module.
<code>c:\Users\User&gt;ipython
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 26 2018, 19:50:54) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import mmap, os

In [2]: with open('test', 'wb') as f:
   ...:     f.write(bytes(1))
   ...:

In [3]: with open('test', 'r+b') as f:
   ...:     m = mmap.mm
