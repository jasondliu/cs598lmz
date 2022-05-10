import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.move(0, 1, 1)
    m.close()
</code>
I know it succeeds if there is a newline (or two) in the file. But if I just have a byte, it seems to fail (the byte disappears).  I want to move byte by byte in a file, not line by line.  Am I doing something wrong?


A:

Your <code>move</code> call is moving a <code>bytes</code> data from position <code>0</code> which is your initial <code>bytes(1)</code> to position <code>1</code> which is the position beyond the end of the file, The destination should exist for <code>move</code> to work and you have to move exactly one byte at a time in this case.
From the <code>mmap</code> documentation
<blockquote>
<p>The mmap module defines the following exceptions:</p>
<p>exception <code>&lt;code&gt;mmap.error&lt;/code&gt;</code>¶ This exception is raised on any mmap related error
