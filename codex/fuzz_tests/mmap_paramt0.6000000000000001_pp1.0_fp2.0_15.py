import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.flush()
</code>
I am getting <code>ValueError: mmap length is greater than file size</code>
What am I doing wrong?


A:

You are getting an error because the file size is too small. 
<code>m = mmap.mmap(f.fileno(), 0)
</code>
is trying to map the whole file into memory.
Try something like this:
<code>m = mmap.mmap(f.fileno(), 128)
</code>
You can find more information on the <code>mmap</code> module here.

