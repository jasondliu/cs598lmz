import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Выдаёт ошибку:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
Почему при закрытии файла закрывается и открытый маппинг? Как это обойти?


A:

Всё дело в том, что маппинг открывается на файловый дескриптор, а не на фа
