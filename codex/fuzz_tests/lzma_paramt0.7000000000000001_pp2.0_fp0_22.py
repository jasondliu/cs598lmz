from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor

from lzma import open as lzma_open

import codecs

def dump(x):
    print(x.__repr__())

#def clear_scr():
    #os.system('cls||clear')

def uncompress(s):
    try:
        return zlib.decompress(s, -15)
    except zlib.error:
        return s

def uncompress_lzma(s):
    try:
        return LZMADecompressor().decompress(s)
    except EOFError:
        return s

def read_file(fname):
    with open(fname, mode='rb') as f:
        return f.read()

def write_file(fname, data):
    with open(fname, mode='wb') as f:
        f.write(data)

def get_bom_size(data):
    from struct import unpack_from
    bom = unpack_from('<H', data, 0)[0]

