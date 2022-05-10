import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    print(m.read_byte())
</code>
Вывод:
<code>49
49
</code>
Он сам преобразует прочитанную байт в код символа, как можно заставить его не делать этого?


A:

Ну наверное, никак нельзя. Тут вам нужно самому преобразовать байт в dec.
Хотя, все же, интересно, почем
