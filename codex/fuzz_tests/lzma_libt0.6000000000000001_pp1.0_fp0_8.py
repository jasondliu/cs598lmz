import lzma
lzma.open()
lzma.open('/path/to/file.xz', mode='w')
lzma.LZMAFile(fileobj=open('/path/to/file.xz', mode='rb'))
lzma.LZMAFile(filename='/path/to/file.xz', mode='rb')
