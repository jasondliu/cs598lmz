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
<code>b'\x01'
</code>
При этом в документации написано, что при создании объекта <code>mmap</code> он получает на вход длину файла. Если я правильно понимаю, значит после того, как файл был обрезан, он должен выдавать пустую строк
