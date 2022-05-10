import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
Вывод:
<code>b'\x01'
</code>

Дополнение
Если посмотреть на реализацию <code>mmap.mmap</code>, то можно заметить, что при инициализации объекта класса <code>mmap.mmap</code> вызывается метод <code>mmap.mmap.flush</code>, который обновляет содержимое
