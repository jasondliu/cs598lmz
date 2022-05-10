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
Получаю ошибку:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Почему происходит ошибка? Как ее исправить?


A:

Потому что вы закрыли файл и не можете получить доступ к нему. Попробуйте изменить код так:
<code>import mmap

with open('
