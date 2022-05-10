import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(len(m))
</code>
output:
<code>8192
</code>
The length of the mapping, as returned by <code>mmap.mmap.size</code> or <code>len(mmap.mmap)</code> never returns 1, and trying to access <code>bytes(m)</code> or <code>str(m)</code> from the mapping raises an <code>OSError</code>. 
I am using <code>mmap.ALLOCATIONGRANULARITY</code> for this example, but even if I set the <code>size</code> argument to a value <code>&lt;= mmap.ALLOCATIONGRANULARITY</code>, the same behavior occurs.
Is there a way to map an array of bytes with elements (independently) directly accessible to <code>bytes(mmap.mmap)</code> or <code>str(mmap.mmap)</code> ?


A:

I believe I have found the answer in http://docs.python.org/release/2.4.4/lib/mmap-example
