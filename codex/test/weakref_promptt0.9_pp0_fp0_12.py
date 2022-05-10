import weakref
# Test weakref.ref, weakref.ProxyType, and weakref.CallableProxyType.
import _weakref
#-----------------------------------------------------------------------------

#
# Symbols captured from expected output should not be checked.
#
# Weakref check: see http://docs.python.org/faq/library.html#how-can-i-test-if-an-object-has-been-garbage-collected
#
# Three possibilities are checked here (in this order):
#
# 1) if module weakref has an attribute ReferenceError, which is used
#    to raise an exception in case of error, we consider the module
#    checked (it is the case for CPython)
#
# 2) if module weakref has an attribute _pending_removals, we use it to
#    check that garbage collection has been done (it is the case for
#    PyPy, should also be for Jython and IronPython)
#
# 3) Otherwise (no specific attribute nicely present), we rely on the
#    garbage collector's own statisitcs, which are available if gc is
#    enabled and if the tracked attribute is not
