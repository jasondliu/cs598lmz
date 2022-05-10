from bz2 import BZ2Decompressor
BZ2Decompressor(); del BZ2Decompressor
#after:
from bz2 import BZ2Decompressor
#optimize:
try:
  from bz2 import BZ2Decompressor
except ImportError:
  BZ2Decompressor=None
if BZ2Decompressor:
  BZ2Decompressor()
  del BZ2Decompressor

#code before:
try:
  from bz2 import BZ2Decompressor
  BZ2Decompressor()
  del BZ2Decompressor
except ImportError:
  pass
#code after:
try:
  from bz2 import BZ2Decompressor
except ImportError:
  BZ2Decompressor=None
if BZ2Decompressor:
  BZ2Decompressor()
  del BZ2Decompressor
