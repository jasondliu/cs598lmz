import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE: https://github.com/dask/dask/issues/2291
#         https://github.com/dask/dask/issues/2291#issuecomment-353727096

# This is a workaround for a bug in numpy.
# See: https://github.com/numpy/numpy/issues/9262
#
# The bug is that when numpy is compiled with the Intel compiler,
# it will raise an exception when a ctypes object is passed to
# a numpy function.
#
# This is a problem for us because we use ctypes objects to represent
# Python objects in the distributed scheduler.
#
# The workaround is to monkey-patch numpy to make it accept ctypes objects.
#
# This monkey-patch is only applied if numpy is compiled with the Intel
# compiler.

# Check if numpy is compiled with the Intel compiler
#
# This is done by checking if the __mkl_version__ attribute exists.
# See: https://software.intel.com/en-us/articles
