import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
</code>
I am trying to replace a byte in a binary file using mmap, but when I read the file, the value is still the original value.
<code>with open('test', 'rb') as f:
    print(f.read()) # outputs b'1'
</code>
Any idea why this happens? It is not a problem of the file not being closed. If I add <code>m.close()</code> after the assignment, the output is still <code>b'1'</code>. 


A:

You need to call <code>m.flush()</code> to make sure the data is written back to the file.

