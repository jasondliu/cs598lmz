import bz2
bz2.compress('Hello, world!') # 'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x06,\x00\x00\x00'
bz2.decompress('x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x06,\x00\x00\x00' ) # 'Hello, world!'

# this module requires that you import the individual Buffer and Compressor subclasses if you want to read and write compressed data to an existing file.
from bz2 import BZ2File
bz = BZ2File('compressed_file.bz2', 'w')
bz.write('Hello, world!')
bz.close()

bz = BZ2File('compressed_file.bz2', 'r')
bz.read() # 'Hello, world!'
bz.close()

# note that the read() call is returning everything at once,
