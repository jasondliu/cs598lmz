import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
На последней строке возникает ошибка
<code>ValueError: mmap closed or invalid
</code>
Собственно, вопрос: почему? Логика, как мне кажется, правильная. Вы ограничиваете длину файла, но картирование в память тем не менее имеет право быть и не может помешать работе с файл
