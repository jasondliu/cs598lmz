import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
На OS X такой код работал. Стоит Debian, он падает. Как можно скопировать содержимое <code>mmap</code> в буфер после транката файла?
Рабочий вариант на Debian выглядит так:

<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as r:
    f = r.read()

    r.seek(0)
    r.truncate()

    with open('test1', 'w+b') as w:
        w.write(
