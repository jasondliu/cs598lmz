import lzma
lzma.decompress(file)
</code>
Но получаю ошибку
<code>TypeError: a bytes-like object is required, not '_io.TextIOWrapper'
</code>
Вопрос: Как декодировать файл?


A:

После выполнения <code>r = open(file_path, 'r')</code> у вас находится объект класса <code>TextIOWrapper</code>, который представляет собой обёртку вокруг бинарного файла, предо
