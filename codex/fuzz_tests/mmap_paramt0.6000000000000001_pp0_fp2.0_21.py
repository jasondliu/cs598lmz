import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
When I open the file (<code>test</code>) in a hex editor, I can see that the file has been extended to 8 bytes instead of the expected 2 bytes.
If I use <code>mmap.mmap(f.fileno(), 1)</code> I get the following error: 
<code>ValueError: mmap length is greater than file size
</code>
What is going on here? I just want to overwrite the existing byte.


A:

You have to open the file in read/write mode.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.write(bytes(2))
</code>

