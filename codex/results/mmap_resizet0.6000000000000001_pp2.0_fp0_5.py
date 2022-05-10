import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
При попытке выполнить последнюю строку возникает исключение:
<blockquote>
<p>OSError: [Errno 9] Bad file descriptor</p>
</blockquote>


A:

Проблема в том, что при создании объекта <code>mmap</code> происходит вызов <code>mmap.mmap.__init__()</code>, который в свою очередь вызывает <code>mmap.mmap.close()</code> после
