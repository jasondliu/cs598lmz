import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    # ValueError: mmap can't resize a readonly or copy-on-write (COW) mapping.
    # m.resize(10)
</code>
Второй вариант с добавлением данных в файл, создание маппинга, уменьшение файла и попытке прочитать добавленные данные:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.write(bytes(10))
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m
