import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # Python (32-bit) SegFaults
</code>
Using mmap like this is safer than using ctypes, since ctypes won't prevent you from trying to access memory that's been unmapped.  It also simplifies the use of <code>mremap()</code>.
Examining the C code for <code>mmap()</code> and <code>_mmap_resize()</code> reveals they're implemented as simple wrappers around Python's (incomprehensible) object-oriented <code>mmapobject</code>.  I can't tell if code like that was always executed when a mapped file was unlinked or truncated, or if that's a bug introduced by a recent change.
<code>tempmem = mmap.mmap(-1, numeric_size,
                    tagname, access=access, offset=offset)
…
tempmem._mmap.close()
</code>
The above is from one of the functions I'm interested in.  You see a reference to <code>tempmem._mmap</code>, which I assume corresponds to an instance of <code>cmmap</
