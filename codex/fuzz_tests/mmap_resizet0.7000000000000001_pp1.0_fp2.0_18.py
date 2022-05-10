import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Запись в файл, создание отображения, урезание файла. При попытке прочитать отображение получаю исключение:
<blockquote>
<p>ValueError: mmap can't expand file to larger than 4294967295 bytes</p>
</blockquote>
Отсюда вопрос: в каких случаях может возникать данная ошибка при использовании mmap?
