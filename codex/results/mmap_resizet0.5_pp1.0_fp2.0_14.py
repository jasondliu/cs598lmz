import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Почему в <code>a</code> всё равно остался байт? Как правильно сделать?


A:

Во-первых, вы забыли закрыть файл после <code>truncate</code>. После этого он перестаёт быть валидным. 
Во-вторых, после того как вы закрыли файл, вы не должны больше испол
