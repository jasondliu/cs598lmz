import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
trying to make a <code>mmap</code> object on a file that is longer than the file is supposed to give some error. However, when I attempt to make an <code>mmap</code> instance on that file and then truncate the file, it doesn't seem to generate any error, and I have a <code>mmap</code> instance which is supposedly larger than the file it is based on.
Is there some way to check whether a file has changed since initializing a <code>mmap</code> object?


A:

As the documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is larger than the current <em>size</em> plus <em>offset</em>, the extended area is filled with zeros.</p>
</blockquote>
So you can grow the file, but you can't shrink it.
If you want a read-write <code
