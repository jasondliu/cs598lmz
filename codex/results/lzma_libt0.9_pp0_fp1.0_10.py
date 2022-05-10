import lzma
lzma.LZMACompressor().compress(b'hello')

# SMAZ compression

from smaz import smaz
smaz.compress('hello')
