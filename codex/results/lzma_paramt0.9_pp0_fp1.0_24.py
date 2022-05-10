from lzma import LZMADecompressor
LZMADecompressor().decompress(settings['volumes'].popitem())

# Заполнили массив файлами дисков и примонтировали их
for i in settings['disks']:
    threading.Thread(target=fill, args=()).start()
</code>
Какой вариант кода правильнее? Или есть способ проще?

