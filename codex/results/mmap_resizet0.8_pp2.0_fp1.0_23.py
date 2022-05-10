import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
Но у меня почему-то читается данные до конца и пишется строка <code>b'\x00'</code>, хотя файл не имеет пробелов. Как найти конец файла с помощью <code>mmap</code>?


A:

Скорее всего вы запускаете скрипт дважды.
Первый раз он пишет в фа
