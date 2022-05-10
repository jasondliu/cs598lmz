import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Не пойму, почему в переменную a попадает именно 0xff. Только если строчку
<code>m = mmap.mmap(f.fileno(), 0)
</code>
заменить на
<code>m = mmap.mmap(f.fileno(), 1)
</code>
тогда значение в переменной a будет 0x0. Можете подсказать?


A:

Именно так работает <code>mmap()</code>. Объект класса <code>mmap</code
