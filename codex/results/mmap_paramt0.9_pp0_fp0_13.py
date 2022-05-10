import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print str(m)[10:-1]
    m.seek(0)
    m.write(bytes(0))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print str(m)[10:-1]
</code>
This works as I expect it to, it prints <code>1</code>, then <code>0</code>.  But I'm still worried that it's not doing what I think it is.  If I create the mmap with a size, e.g.
<code>m = mmap.mmap(f.fileno(), 1)
</code>
it seems like it might be reading from the wrong place, even though I am eventually writing at the correct place.
I just don't know how mmap works, and I don't want to guess (and therefore get it wrong).


A:

Functions like <code>read</code> and <code>write</code> will move the file's <code>seek</code> position. <code>m.tell()</code>
