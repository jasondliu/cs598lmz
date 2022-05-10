import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
При попытке обратиться к <code>m</code> получаю ошибку:
<code>    a = m[:]
UnboundLocalError: local variable 'm' referenced before assignment
</code>
Содержимое <code>test</code> не изменилось. Как это исправить? Где ошибка?
Заранее спасибо.


A:

Функция <code>truncate()</code> нужно вызывать уже после установки <code>mmap</code>.
<code>from mmap import
