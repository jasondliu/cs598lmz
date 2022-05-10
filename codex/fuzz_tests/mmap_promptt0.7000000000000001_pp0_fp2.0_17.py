import mmap
# Test mmap.mmap(0, 4096, "a", mmap.MAP_PRIVATE, -1, 0)

with open("/tmp/text", "w") as f:
    f.write("foo")

m = mmap.mmap(0, 4096, "a", mmap.MAP_PRIVATE, -1, 0)
m.write("bar")
m.seek(0)
print(m.read())
</code>

<code>$ python test_mmap.py
bar
</code>

Notes:

I'm on a Linux machine (Ubuntu 16.04)
I'm using Python 3.5.2
This is a toy script to illustrate the problem



A:

You are not calling <code>mmap.mmap()</code> correctly. The <code>fd</code> argument is the file descriptor of an open file, not the file name.
<code>import os
import mmap

filename = "/tmp/test_mmap"

with open(filename, "w") as f:
    f.write("foo")

with open
