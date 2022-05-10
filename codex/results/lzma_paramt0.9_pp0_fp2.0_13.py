from lzma import LZMADecompressor
LZMADecompressor().decompress(b'./xz_decoded_data')

def do_something_neat(b):
    return b[5] + b[10] + b[50] + b[100] + b[150]

try:
    xz_decoder.add_callback(do_something_neat)
except TypeError:
    print("TypeError")
</code>
После декодирования данных из файла размером в 6MB выдает ошибку "OverflowError: size does not fit in an int".


A:

Решил проблему тем, что нашел модуль <code>liblzma</code> и использовал его
