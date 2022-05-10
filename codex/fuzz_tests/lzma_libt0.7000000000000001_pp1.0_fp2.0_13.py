import lzma
lzma_file = lzma.LZMAFile('/home/dongyue/prog/data/google-books-common-words.txt.xz')
lines = lzma_file.readlines()
lines[:10]

#lines.count(b'i\r\n')
#lines.count(b'the\r\n')
#lines.count(b'be\r\n')
#lines.count(b'to\r\n')
#lines.count(b'of\r\n')
#lines.count(b'and\r\n')
#lines.count(b'a\r\n')
#lines.count(b'in\r\n')
#lines.count(b'that\r\n')
#lines.count(b'have\r\n')
#lines.count(b'I\r\n')
#lines.count(b'it\r\n')
#lines.count(b'for\r\n')
#lines.count(b'not\r\n')

