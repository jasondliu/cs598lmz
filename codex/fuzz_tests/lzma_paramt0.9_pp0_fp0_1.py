from lzma import LZMADecompressor
LZMADecompressor().decompress(pdf.decode('hex'))
pdf

from mimetypes import guess_type

guess_type(
    'http://ejuz.net.cn/media/3f3g3f3g3gg3gd3gdgdfdfdf34hgggdfdffdfd/111111111/image_c.pl?imageId=123456789012&amp;z=0.1',
    strict=True)

guess_type(
    'http://ejuz.net.cn/media/3f3g3f3g3gg3gd3gdgdfdfdf34hgggdfdffdfd/111111111/image_b.pl?imageId=123456789012&amp;z=0.1',
    strict=True)


test_jpg = '\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C
