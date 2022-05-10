fn = lambda: None
# Test fn.__code__.co_argcount
arg
# Test fn.__code__.co_filename
arg
# Test fn.__code__.co_firstlineno
arg

# Test for Numeric and numpy.numarray. In our testing, num arrays are
# always single dimensional and of type float64.
#
# @param a
#   The array to check
# @returns
#   True if the argument is a numarray or Numeric.
#
def is_num_array(a):
# Can't do numarray stuff if numarray isn't available
  if not NUMARRAY_AVAILABLE:
    return false
  if isinstance(a, numpy.ndarray) or isinstance(a, Numeric):
    if len(a.shape) == 1:
      if a.dtype == 'float64':
        return true
return false

# TODO: Clean up the memory created during these tests.
# Copy the file to hdf5 format
copy_to_hdf5(raw_name, h5, *arg)
# Create a new temp filename
fname =
