import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    m[0] = ord(b'A')
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Вывод в консоль:
<code>b'A'
</code>
Но если размер файла больше 1 байта, то размер файла не меняется. Пример:
<code>with open('test', 'wb') as f:
    f.write(bytes(2))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    m[0] = ord(b'A')
    m.close()

with open
