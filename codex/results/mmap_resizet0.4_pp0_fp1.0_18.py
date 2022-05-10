import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I thought the mmap is not affected by truncate.
Is this a bug?


A:

You're not allowed to truncate a file that is mmapped. From the docs:
<blockquote>
<p>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])<br/>
  ...<br/>
  The file must be opened in read/write (“r+”) mode. <strong>size is ignored</strong> and the current size of the file is used instead.</p>
</blockquote>
(emphasis mine)

