import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # segfault
</code>
If the last line is commented out (or Python version is downgraded) then it works.
Question: Is this a bug in Python 3.4 or what? More importantly, how can I work around this?!


A:

I'm trying to test this on a 32 bit system (Windows 7), with Python 3.4.0, and mmap 0.9.3.
I can't reproduce this; it works fine.
One thing I noticed you didn't do is put an explicit size for the mmap; for example, you might want to try this, because the length of the data in the file matters:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    f.truncate()
    m[:] = bytes(1) # segfault
</code>

