import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'rb') as f:
    b = f.read()
</code>
When the above code is executed, <code>a</code> equals <code>1</code>, while <code>b</code> equals <code>0</code>. Somehow it seems that the mmap object is mapping the file even after the file is truncated. 
I am aware that the mmap module documentation says that:
<blockquote>
<p>Once a mapping is removed, attempts to access the corresponding range
  of the mapped file using mmap objects or other means may raise SIGBUS
  (Linux, BSD), produce undefined results (Solaris), or result in a
  read from the original file (Mac OS X).</p>
</blockquote>
However is there a way to obtain the same value for <code>a</code> and <code>b</code> after truncating the file?


A:

I can't reproduce your result.  If I run the following script:
<code>#!/usr/bin/python3

import mmap

with open('test', 'wb')
