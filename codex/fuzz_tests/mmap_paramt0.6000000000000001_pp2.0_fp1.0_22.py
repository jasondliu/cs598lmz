import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
При запуске программы получаю ошибку:
<code>Traceback (most recent call last):
  File "C:/Users/User/PycharmProjects/untitled/test.py", line 6, in &lt;module&gt;
    m.write(bytes(2))
TypeError: write() argument must be a bytes-like object, not 'int'
</code>
В чём проблема?


A:

Потому что <code>bytes</code> в Python 3 - это не тип, а встроенная функция. Если вы передаёте ей числ
