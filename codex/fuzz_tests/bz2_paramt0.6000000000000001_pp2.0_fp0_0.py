from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Для использования собственного декомпрессора последовательность байтов декомпрессируется функцией decompress() из модуля zlib.
# Если данные не представляют собой корректно сжатую последовательность байтов, то будет вызвано исключение zlib.error.
#
