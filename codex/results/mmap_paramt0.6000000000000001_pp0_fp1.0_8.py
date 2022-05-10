import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))

    m.seek(0)
    m.write(bytes(2))

    m.seek(0)
    print(m.read(1))
</code>
Все работает, но если я укажу длину больше одного байта, то программа не завершается:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m.read(1))

    m.seek(0)
    m.write(bytes(2))

    m.seek(0)
    print(m.read(1))
</code>
Почему?


A:

Вызов <code>mmap
