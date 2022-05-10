import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Пытаюсь получить содержимое открытого файла после того как его обрезал. Выдает ошибку <code>mmap.error: [Errno 22] Invalid argument</code> на строке <code>a = m[:]</code>


A:

После <code>truncate</code> объект <code>m</code> указывает на новый созданный файл. Объект <code>m</code> является неизменным.
