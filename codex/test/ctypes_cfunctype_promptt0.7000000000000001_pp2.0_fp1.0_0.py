import ctypes
# Test ctypes.CFUNCTYPE()
#
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False, winmode=0)
#
#    restype
#        The result type of the callback function.
#
#    argtypes
#        The argument types of the callback function.  A list of type
#        objects or a single type object may be used.
#
#    use_errno
#        If true, the callback function will get errno as a third parameter.
#
#    use_last_error
#        If true, the callback function will get GetLastError() as a third
#        parameter.  This is ignored on Windows.
#
#    winmode
#        If true, the callback function will be passed a keyword
#        parameter named 'flags' which will be assigned the integer
#        value of the MS_WIN32_OR_HIGHER_ONLY flag if the callback
#        is being called from 32-bit Python on a 64-bit Windows system,
#        or the integer value 0 otherwise.
#
#        This
