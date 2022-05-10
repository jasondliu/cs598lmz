import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
А этот бросает исключение:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>
Можно ли как-то обновить размер файла в менеджере контекста после создания объекта <code>mmap</code>?


A:

Посмотрите документацию к <code>mmap.mmap.resize
