import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)

</code>
The output on Linux is:
<code>b'\x01'
</code>
The output on Windows is:
<code>b''
</code>
(The expected output on Windows is also <code>b'\x01'</code>.)
On Windows, we need to somehow remove the limitation to prevent the error.


A:

As in the comments of the question, the root cause is a limitation of the Windows function <code>CreateFileMappingNuma</code>.
The limitation is that the offset and size need to be a multiple of the system information <code>AllocationGranularity</code>.
<code>CreateFileMappingNuma</code> is called by <code>mmap.mmap</code> and <code>mmap.mmap_win</code>.
Thus, the size needs to be a multiple of this number.
This is not a problem on Linux, because Linux is less restrictive.

