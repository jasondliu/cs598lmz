import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Throws a "ValueError: mmap offset is greater than file size". I assume that the value is too big because some data is appended when the file is truncated, but I don't see why mmap requires seeking to the end anyway.
P.S. Why does python assume that <code>with open(file) as f</code> will set <code>f</code> to a file object that actually is the passed filename? Even <code>os.fdopen</code> does not enforce that.


A:

<blockquote>
<p>Why does python assume that with open(file) as f will set f to a file object that actually is the passed filename?</p>
</blockquote>
For that matter, why does Python assume <code>f</code> will ever be a file object?
<code>with</code> is not a "magic" statement. It's a block of code, and in your example there are two separate blocks, the enter block and the exit block.
The <code>with</code> statement executes the <code>as</code> expression, meaning <code>open(file
