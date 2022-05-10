import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(m, a)
</code>
Results in <code>mmap.error: cannot modifiy size of memory map</code>
Can I solve this without needing to unmap the memory map before calling <code>truncate</code> or some other solution? If not, can it be included in the python standard library?
I know that I can avoid several closures if I change the code to
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
but I would like to avoid having to close the <code>mmap</code> object in every position where this happens, and rely on context managers.


A:

It is not possible to flush the contents of a memory map to the file without un-mapping the memory map first. 

