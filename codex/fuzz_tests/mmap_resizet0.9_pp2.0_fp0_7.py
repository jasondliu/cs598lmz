import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 22] Invalid argument
</code>
The documentation says that the file is supposed to be read only after <code>truncate()</code>, but it is open in 'r+b'.


A:

On POSIX: you must use <code>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])</code>:
<blockquote>
<p><code>&lt;code&gt;prot&lt;/code&gt;</code> - Specifies the level of access; it must be one of <code>&lt;code&gt;PROT_READ&lt;/code&gt;</code>, <code>&lt;code&gt;PROT_WRITE&lt;/code&gt;</code>, or <code>&lt;code&gt;PROT_EXEC&lt;/code&gt
