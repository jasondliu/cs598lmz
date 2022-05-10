import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
В Linux все нормально - a = b''
В Windows вылетает исключение:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Подскажите плиз, как можно освободить буфер в ОС, чтобы прочитать содержимое?


A:

Проблема в моменте:
<code>a = m[:]</code>
Нужно использовать метод <code>read</code> так как <code>mmap</code> не и
