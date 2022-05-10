from bz2 import BZ2Decompressor
BZ2Decompressor.__init__=BZ2Decompressor___init__
del BZ2Decompressor___init__
import bz2
bz2.BZ2Decompressor.__init__=BZ2Decompressor___init__
del BZ2Decompressor___init__
import bz2
del bz2.BZ2Decompressor.__init__

def BZ2Decompressor___read__(self, *args, **kwargs):
  global monkey_BZ2Decompressor_old_callback
  ret = None
  if monkey_BZ2Decompressor_old_callback:
    ret = monkey_BZ2Decompressor_old_callback(self, *args, **kwargs)
  else:
    ret = self.__orig_read__(*args, **kwargs)
  return ret

BZ2Decompressor___orig_read__ = BZ2Decompressor.read
BZ2Decompressor.__orig_read__ = BZ2Decompressor.read
BZ2Decompressor.read = BZ2Decomp
