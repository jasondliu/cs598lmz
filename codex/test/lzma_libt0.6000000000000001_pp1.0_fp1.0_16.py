import lzma
lzma.LZMACompressor()

import copyreg
copyreg.pickle(type(lambda: 0), lambda obj: (lambda: 0, ()))

import marshal
marshal.dumps(0)

import math
math.atan2(0,0)

import mmap
