import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.resize(1)
    b = m[:]

with open('test', 'rb') as f:
    c = f.read()

print len(a), len(b), len(c)
</code>
This produces:
<code>1 0 0
</code>
When I expect it to be:
<code>1 1 1
</code>
There doesn't seem to be any mention of this in the documentation.  Is this a bug, or am I doing something wrong?
I'm using Python 2.7.6.  I don't have any version of Python 3 available to test this.
Edit:
The other answers are all good, and the <code>truncate</code> function of the file object is the only reason this isn't working.  I've been working with mmap files for a bit now, and have found that because of the two independent buffers, you can get some unexpected results if you make changes without being careful.
In the example above, resizing the mmap buffer is actually changing the size of the file, but read after that will return the data that was originally in the mmap buffer
