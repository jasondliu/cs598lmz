import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: mmap can't extend a read-only or copy-on-write file mapping</code> on the last line.
I can't find anything in the docs about this.  Is there a way to get around this?  I'm on Python 3.4.3.

