import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Вывод:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Как после усечения файла правильно получить данные из маппинга?

