import bz2
bz2.decompress(data)

# bz2.decompress(data)
# TypeError: argument 1 must be string or read-only buffer, not bytes

# bz2.decompress(data.decode('utf-8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 10: invalid start byte

bz2.decompress(data.decode('latin-1'))

# bz2.decompress(data.decode('latin-1'))
# TypeError: argument 1 must be string or read-only buffer, not bytes

bz2.decompress(data.decode('latin-1').encode('utf-8'))

# bz2.decompress(data.decode('latin-1').encode('utf-8'))
# TypeError: argument 1 must be string or read-only buffer, not bytes

bz2.decompress(data.decode('latin-1').encode('utf-8').decode('utf-
