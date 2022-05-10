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
Попробовал сделать пример по подобию из документации по mmap, но там используется строка, а мне нужно сделать это с байтами.
Есть ли возможность правильно сделать это?
Спасибо!


A:

Вот этот код работает:
<code>import mmap

with open('test', 'wb') as f:

