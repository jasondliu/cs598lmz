import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

#The above code will print:
#b'This is the content.'

#compress
import lzma
lzma.compress(b'This is the content.')

#The above code will print:
#b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'

#compress
import lzma
lzma.compress(b'This is the content.', format=lzma.FORMAT_ALONE)

#The above code will print:
#b'\x00\x04\xe6\xd6\xb4\x
