fn = lambda: None
# Test fn.__code__ was introduced in 3.3, but some older 3.x versions
# have it anyway
try:
  getattr(fn, '__code__')
  HAVE_CODE_TYPE = True
except AttributeError:
  HAVE_CODE_TYPE = False

try:
  import numpy
  HAVE_PY_ARRAY = True
  ARRAY_CTYPE = numpy.dtype(ARRAY_INT_CTYPE)
  ARRAY_PYTYPE = ARRAY_INT_CTYPE
except ImportError:  # If we can't get numpy, fall back to array
  HAVE_PY_ARRAY = False
  import array
  ARRAY_CTYPE = array.array(ARRAY_INT_CTYPE)
  ARRAY_PYTYPE = getattr(ARRAY_CTYPE, 'typecode', None)
  if not HAS_BUFFER_PROTO or not PY3:
    HAVE_PY_ARRAY = False


#
# A heap-based priority queue
#
class PriorityQueue:
  """PriorityQueue([
