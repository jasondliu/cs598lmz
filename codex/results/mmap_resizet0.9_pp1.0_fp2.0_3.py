import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Во втором случае выводится пустая строка, как и ожидалось. Если убрать строку <code>f.truncate()</code>, то так же, что и в первом случае выводится <code>b'\x01'</code>
Вопрос: почему второй случай связан с триггерным исключением? И почему в первом слу
