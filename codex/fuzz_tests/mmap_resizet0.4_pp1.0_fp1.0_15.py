import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
Вывод:
<code>b'\x00'
</code>
Ожидал:
<code>b'\x01'
</code>
Почему так? Как сделать правильно?

