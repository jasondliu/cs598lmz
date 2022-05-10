import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a hack to force the object mode runtime to be used.  It
# works because ctypes.py_object is present only in the new-style
# class for Python 2.2.
#
# Note: This is not needed anymore since PyPy 1.6.
#
# See also:
# http://codespeak.net/pipermail/pypy-dev/2010-January/008819.html
# http://codespeak.net/pipermail/pypy-dev/2010-January/008820.html
# http://codespeak.net/pipermail/pypy-dev/2010-January/008822.html
# http://codespeak.net/pipermail/pypy-dev/2010-January/008823.html
# http://codespeak.net/pipermail/pypy-dev/2010-January/008824.html
# http://codespeak.net/pipermail/pypy-dev/2010-January/008825.html
# http://codespeak.
