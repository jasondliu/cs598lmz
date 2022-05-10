import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect the variable <code>a</code> to contain the number <code>1</code> (in bytes), but instead it's only showing me garbage. The file <code>test</code> itself is empty.
Why is this happening? It looks like the truncation (which happens on the open file object itself) got propagated to the mmap object.


A:

Doing the following seems to work fine:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    # Create an mmap object
    m = mmap.mmap(f.fileno(), 0)
    # Close the file
    f.close()
    # Read the byte
    byte = m.read(1)
    # Close the mmap
    m.close()
</code>
According to open(2):
<blockquote>
<p>The file offset used by mmap(2) is relative to the beginning of the file, not to the start of mapping.</p>
</
