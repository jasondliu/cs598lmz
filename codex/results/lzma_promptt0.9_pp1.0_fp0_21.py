import lzma
# Test LZMADecompressor()
lzc = lzma.LZMADecompressor()

#f = open('outfile.lzma', 'rb') # файл для чтения
#f.read(5)  # прочитать пять байт файлов

file = open('outfile.lzma', 'rb')
contents = file.read()
decompressed_data = lzc.decompress(contents)
data = decompressed_data.decode("UTF-8")
data = data.split('\n')
file = open('decompr.txt', 'w')
file.write(str(data))
# lzma -s example.txt    # Создает exampl2.txt.lzma, сжатую в стандартном режиме с максим
