import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Как видите, в <code>a</code> оказалась пустая строка. Это из-за того, что в момент <code>f.truncate()</code> вызывается метод <code>mmap.mmap.close()</code>, который вызывает системный вызов <code>munmap</code>. Вот документация по нему:
<blockquote>
<p>munmap() deletes the mappings for the specified address range, and causes further references to addresses within the range to generate invalid memory references. The region is also automatically unmapped when the process is terminated.</p>
<p
