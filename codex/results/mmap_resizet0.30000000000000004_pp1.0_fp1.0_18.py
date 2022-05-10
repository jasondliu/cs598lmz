import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
При выполнении последней строки получаю ошибку:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Почему так происходит? Как можно получить данные из файла после его урезания?


A:

Вот так получилось:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with
