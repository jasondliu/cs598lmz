import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(10))
</code>
I expect the file to be filled with 10 times the digit 1 (i.e. <code>1111111111</code>), but instead I get something like <code>??????????</code>.
If I write the buffer directly to the file:
<code>with open('test', 'wb') as f:
    f.write(bytes(10))
</code>
I get the expected result.
Why can't I write the bytes to the memory map?


A:

You need to use the <code>mmap.resize()</code> method to extend the mapped region of the file first before trying to write the entirety of the new bytes:
<code>m = mmap.mmap(f.fileno(), 0)
m.resize(10)
m.write(bytes(10))
</code>

