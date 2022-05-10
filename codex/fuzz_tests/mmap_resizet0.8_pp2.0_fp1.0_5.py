import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print("exit")
</code>
I get the following error when running this code:
<code>mmap.error: [Errno 22] Invalid argument
</code>
However, if I use <code>mmap.mmap(f.fileno(), 1)</code>, it works.
I checked the <code>mmap.error</code> class and it has the following comment:
<code># Allow the length to be zero to support opening empty mmap instances
</code>
However, this doesn't work for me.


A:

The documentation states:
<blockquote>
<p>If length is 0, the maximum length of the map will be the current size of the file when mmap is called. </p>
</blockquote>
The following might help:
<code>import os
import mmap

# create file
with open('test', 'wb') as f:
    f.write(bytes(1))

# truncate file
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access
