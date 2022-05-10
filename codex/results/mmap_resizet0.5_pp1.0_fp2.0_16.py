import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This results in a <code>ValueError: mmap offset is greater than file size</code>.
I was able to reproduce this on Python 3.4.2, 3.5.2 and 3.6.0.
I know that I can use <code>mmap.resize</code>, but I don't want to do that because I don't want to lose the data.
I also know that I can achieve what I want by calling <code>m.flush()</code> before truncating the file, but I want to avoid doing that if possible.
Is there any way to truncate a file that is mmap'd in r+b mode without losing the data?

