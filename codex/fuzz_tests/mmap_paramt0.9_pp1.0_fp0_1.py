import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0xfa
    m.flush()
m.close()
</code>
The python docs also state that:
<blockquote>
<p>When using mmap, one must be careful to only access the mapped slice of the view: not to exceed it or to access a sensitive area of the file.</p>
</blockquote>
So writing outside of the mapped section could potentially have detrimental effects.


