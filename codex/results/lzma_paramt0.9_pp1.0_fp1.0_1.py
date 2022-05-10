from lzma import LZMADecompressor
LZMADecompressor()

import zlib
ZlibDecompressor()

import bz2
bz2.BZ2Decompressor()

# math
import fractions
fractions.Fraction(0, 1)


# cmath, math, decimal and fractions
complex(333.333, 0.3333)

math.floor(0.7)
math.log(10, 2)
math.log(100, 10)

import decimal
dec = decimal.Decimal(-3.14)

dec = dec.quantize(decimal.Decimal(1), rounding=decimal.ROUND_UP)

import fractions
f = fractions.Fraction(1, 3)
f

# os, pathlib
import os
os.chdir('..') # changes current directory
os.curdir # current directory
os.listdir(os.curdir) # lists current directories

import glob
glob.glob('*.py') # list all python files

import pathlib
p = pathlib.Path('.')
p.iterdir()

# itertools, funct
