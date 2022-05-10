import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Данный код говорит нам, что <code>m[:]</code> возвращает байтовую строку <code>b'\x00\x00\x00\x00'</code> (пустая строка из 4 нулевых байтов), хотя файл был с одним байтом. Это значит, что при изменении размера файла файловой системой карта файл
