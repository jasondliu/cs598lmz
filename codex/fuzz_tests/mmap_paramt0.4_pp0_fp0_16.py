import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.flush()
</code>
The file is not written.
I have tried to use <code>m.seek(0)</code> before <code>m.write</code> and <code>m.close()</code> after <code>m.flush()</code>, but it didn't help.
I have also tried to use <code>m.seek(0)</code> and <code>m.write(bytes(1))</code> in a loop, but it didn't help either.
I have also tried to use <code>m.seek(0)</code> and <code>m.write(bytes(1))</code> in a loop with <code>m.flush()</code> and <code>m.close()</code> after each iteration, but it didn't help either.
I have also tried to use <code>m.seek(0)</code> and <code>m.write(bytes(1))</code> in a loop with <code>m.flush()</code> and <code>m.close()</code> after
