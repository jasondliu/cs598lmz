import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # error
</code>
Вывод:
<code>Traceback (most recent call last):
  File "mmap.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: couldn't find value
</code>
Почему не закрывается соединение карты с файлом?


A:

Потому что надо явно закрывать. Что-то типа:
<code>with open('test', 'r+b') as f, mmap.mmap(f.fileno(), 0) as m:
    hand.truncate()
    a = m[:]
</code>
в приведенном примере создаетс
