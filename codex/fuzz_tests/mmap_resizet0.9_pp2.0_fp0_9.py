import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
На первой строке открываем файл на запись из байтов. Как вы и рекомендует документация, мы используем байты, а не строку, так как работаем с байтовыми данными. На следующей строке открываем файл на обычный чтение и запись.
