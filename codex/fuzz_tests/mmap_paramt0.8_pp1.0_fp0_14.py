import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] == 1 # This returns True
    f.seek(0) # This doesn't work, f.tell() is still 0
    f.tell() # This returns 0
</code>
Why is this happening? How to fix this?


A:

I think you need to flush the buffers.
<code>m.flush()
</code>

