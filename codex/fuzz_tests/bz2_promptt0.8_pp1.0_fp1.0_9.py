import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    with smart_open.smart_open('wiki.ru.bz2') as f_in:
        with open('wiki.ru', 'wb') as f_out:
            while True:
                block = f_in.read(1024)
                if not block:
                    break
                f_out.write(decompressor.decompress(block))
!ls

!head -n 3 wiki.ru

# несжатый вариант файла
!mv wiki.ru wiki.ru.txt

with smart_open.smart_open('wiki.ru.bz2') as fin:
    for line in fin:
        print(line)
        break

# неудобно, если размер файла в байтах - не степень 2


