import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Выводит <code>b'\x00'</code>.
Почему выводит не пустой байтовый массив?


A:

<code>mmap</code> представляет собой обертку над системным вызовом <code>mmap</code> (на винде <code>CreateFileMapping</code>), который позволяет отобразить любой файл в память. При этом в памяти отображае
