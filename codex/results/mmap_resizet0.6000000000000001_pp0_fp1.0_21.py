import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Вывод:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
TypeError: an integer is required (got type bytes)
</code>
Вопрос: почему не работает? И как правильно получить содержимое файла после обрезания?


A:

Как выяснилось, при создании объекта <code>mmap</code> картируется только часть файл
