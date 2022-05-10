import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm expecting the <code>IndexError</code> to be raised, but Python executes the code without errors. If I remove <code>f.truncate()</code> call, the <code>IndexError</code> would be raised.
Is it possible to crash the process (if I don't know the file contents) with <code>mmap</code>, or is it always safe to do things like that?


A:

There is documentation for <code>mmap</code> on this page.
Search it for <code>fileno</code> and you will see that using <code>mmap</code> you get a copy of the data in the file:
<blockquote>
<p>mmap.mmap(fileno, length[, access[, offset]])</p>
<p>Create a memory-map to an
  existing <strong>file</strong>. <em>fileno</em> is an open <strong>file descriptor</strong> and it <strong>must be
  open for either reading or writing</strong> (or both), depending on whether
  you want a read
