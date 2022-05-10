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
<code>b'\x01'
</code>
То есть, после выполнения операции <code>f.truncate()</code>, данные маппинга не обнуляются, а остаются в памяти.
Вопрос:
Почему это происходит? Как я понял из документации, при изменении размера файла данные маппин
