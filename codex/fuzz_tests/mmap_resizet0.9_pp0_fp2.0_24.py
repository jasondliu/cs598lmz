import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # &lt;----------------------------- segfault
</code>
The question: how could the memory map be closed after <code>truncate</code>-ing the file, so that the invalid access (<code>m[:]</code>) above could raise a <code>mmap.error</code>?
P.S.: there are two solutions I can come with:

call <code>m.resize()</code> before <code>truncate()</code> (Approach 1)
call <code>f.flock(LOCK_EX)</code> before <code>m[:]</code> (Approach 2)

The problem is: I don't know if there is a more elegant way (Approach 3), because approaches 1 and 2 are rather hacky. I'm also looking for a more detailed explanation of the problem.
P.P.S: I run Python 3.6.4 on Alpine Linux 3.6.2


A:

First I'd like to state that you must be seeing undefined behavior here.  The behavior of a program with a data race (such as this one) is undefined.  Undefined
