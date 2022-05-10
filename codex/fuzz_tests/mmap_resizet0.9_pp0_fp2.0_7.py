import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # This crashes with a SIGSEGV
</code>
The same crash happens for <code>mmap.PROT_READ</code> and <code>mmap.PROT_EXEC</code> instead of <code>mmap.PROT_WRITE</code>.


A:

The following should at least be helpful to understand what is happening here. It adapts the <code>example-memmap.py</code> to your scenario: 
<code>#!/usr/bin/python
"""
Demonstrate the use of mmap to create a writeable mmap as well as a
read-only mmap to the same file.
"""

import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    ro = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate() # not needed?
    assert ro.closed == 0 # check for closed-state in ro
    f.write(b'12345
