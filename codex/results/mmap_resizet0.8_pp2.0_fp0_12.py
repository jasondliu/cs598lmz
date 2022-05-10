import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
From the documentation:
<blockquote>
<p>If you modify a file after you first map it, some implementations
  update the mapping in place, so your modifications will be visible
  through the mapping; others create a new mapping to reflect the new
  file contents, so modifications are not visible through the mapping.</p>
</blockquote>
Does this mean that I need to check whether a new mapping was created, or how do I know whether <code>m[:]</code> will return the original (now deleted) bytes or the new empty bytes?
UPDATE:
It seems like behavior varies by OS. Ubuntu (with Python versions 2.7.6, 2.7.9, 3.4.1) seems to be one category and Windows (versions 2.7.9, 3.4.2) another.
UPDATE2:
A comment suggested I could use <code>f.seek(0,0)</code> to determine if a new mapping was created. However, the following code outputs 0, even though a new mapping was created on Windows:
<code>#!/usr/bin/env python2

