import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Вывод:
<code>b'\x00'
</code>
Почему выводится не <code>b'\x01'</code>?


A:

Потому что вы пытаетесь читать из файла, который вы уже обрезали.
После выполнения <code>f.truncate()</code> файл пустой, и нет никаких данных для чтения.
Как вариант, можно проч
