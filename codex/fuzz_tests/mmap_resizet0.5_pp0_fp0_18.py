import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Выбрасывается исключение <code>mmap.error: [Errno 22] Invalid argument</code>. И в Python 3.5 всё так же. Но если добавить <code>m.close()</code> в конце, то всё работает. Но при этом становится невозможным получить <code>a</code> в виде <code>bytes</code> (приходится использовать <code>a = m.read()</code>).
Вопрос: почему н
