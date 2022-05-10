from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)


import bz2
bz2.decompress(s)


#Encoding
# Python uses ASCII as the default when working with strings, meaning anything not in the ASCII character set is represented as a \x value.
# Python 3 uses Unicode instead of ASCII.

s = 'pýtĥöñ\fis\tawesome\r\n'
s

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}

a = s.translate(remap)
a

import unicodedata

unicodedata.normalize('NFD', a)


b = unicodedata.normalize('NFD', a)
b

b.encode('ascii', 'ignore').decode('ascii')

# remove all diacritical marks
def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = '
