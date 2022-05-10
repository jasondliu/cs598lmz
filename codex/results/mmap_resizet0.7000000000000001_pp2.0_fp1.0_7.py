import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Ожидаемым результатом будет <code>b'\x00'</code>, получаем <code>b'\x01'</code>.
Если убрать строку <code>m[:]</code>, то всё будет работать как надо.
Почему такое случается?
Это неожиданное поведение или я не так знаю спецификацию?


A:

Если вы создадите
