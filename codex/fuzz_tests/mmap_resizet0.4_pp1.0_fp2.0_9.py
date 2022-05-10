import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Пишет ошибку:
<code>Traceback (most recent call last):
  File "C:/Users/Александр/PycharmProjects/untitled/test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Как это исправить?


A:

После транката файла нужно заново открывать маппинг.
Вот пример кода, который проверяет, что файл пустой, и если
