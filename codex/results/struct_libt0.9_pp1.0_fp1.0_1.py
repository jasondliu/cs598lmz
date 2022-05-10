import _struct, _array

_types = (
 'c', 'b', 'B', 'u', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd'
)

_array_types = {
 'c': '1s',
 'b': 'b',
 'B': 'B',
 'u': 'H',
 'h': 'h',
 'H': 'H',
 'i': 'i',
 'I': 'I',
 'l': 'l',
 'L': 'L',
 'f': 'f',
 'd': 'd'
}

def _clearcache():
  try:
    del _struct._clearcache.im_func
  except AttributeError:
    pass


def calcsize(fmt):
  return _struct.calcsize(fmt)


def pack(fmt, *args):
  return _struct.pack(fmt, *args)


def pack_into(fmt, buf, offset, *args):
  s = pack(fmt, *args)
