import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(5)
    m.flush()
    m.close()
</code>
Is there a better way to accomplish what I'm trying to do? Do I need to flush the file like I am doing?


A:

<blockquote>
<p>Is there a better way to accomplish what I'm trying to do?</p>
</blockquote>
It depends on what exactly you're trying to do. From the title, it seems you're trying to update a single bit in a file. If that's so, then you're doing it exactly the right way.
<blockquote>
<p>Do I need to flush the file like I am doing?</p>
</blockquote>
Yes.

