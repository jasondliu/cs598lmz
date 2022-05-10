import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Выводит <code>b'\x00'</code>
Как я понимаю, при уменьшении размера файла все данные после этого размера просто обнуляются. Вопрос: как выбросить их из памяти? Или можно ли это сделать вообще?

