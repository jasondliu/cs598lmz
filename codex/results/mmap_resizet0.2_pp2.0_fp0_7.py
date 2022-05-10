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
<code>b'\x00'
</code>
Но если поменять местами две последние строки, то вывод будет:
<code>b'\x01'
</code>
Почему так происходит? Как можно объяснить такое поведение?


A:

Потому что при вызове <code>f.truncate()</code> не происходит обрезки файла, а пр
