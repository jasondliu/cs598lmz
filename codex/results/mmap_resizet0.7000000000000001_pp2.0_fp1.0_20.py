import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
    print(a == b)
</code>
This code return <code>True</code> but I expect <code>False</code>.
From the docs:
<blockquote>
<p>In the normal case, mmap objects can be used anywhere a string is expected; <strong>for read-write access, a string object must be used to modify the buffer</strong></p>
</blockquote>
I assume that <code>a = m[:]</code> is using the <code>m</code> reference to create a new string and not a reference, but that is not the case.
What is the best way to make a copy of the mmap?


A:

<blockquote>
<p>I assume that a = m[:] is using the m reference to create a new string and not a reference, but that is not the case.</p>
</blockquote>
the output <code>True</code> is correct.
<code>a = m[:]</code> is using the <code>m</code> reference to create a new string and not a reference.

