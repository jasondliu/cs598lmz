import ctypes
# Test ctypes.CFUNCTYPE(None)
# Note that this is not a valid test case with the current implementation
# of ctypes.  The CFUNCTYPE(None) factory function currently returns an
# instance of the _CFuncPtr class, which is not callable.  It is not
# callable because it has no _flags_ attribute.  The _flags_ attribute
# is set by the constructor of the _CFuncPtr class, which is never called
# because the _CFuncPtr class is not a callable class.  The _CFuncPtr class
# is not callable because it is not a sub-class of _CFuncPtrBase.
# The _CFuncPtrBase class is not callable because it has no _flags_ attribute.
# The _flags_ attribute is set by the constructor of the _CFuncPtrBase class,
# which is never called because the _CFuncPtrBase class is not a callable class.
# The _CFuncPtrBase class is not callable because it is not a sub-class of
# _CDataMeta.  The _CDataMeta class is not callable because it has no
# _flags_
