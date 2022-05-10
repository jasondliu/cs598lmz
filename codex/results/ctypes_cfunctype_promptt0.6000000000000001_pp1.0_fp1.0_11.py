import ctypes
# Test ctypes.CFUNCTYPE()
#
# Let's try to call the Win32 GetSystemTimeAsFileTime() function, which
# has the following signature:
#
#    void GetSystemTimeAsFileTime(LPFILETIME lpSystemTimeAsFileTime)
#
# where FILETIME is defined as:
#
#    typedef struct _FILETIME {
#        DWORD dwLowDateTime;
#        DWORD dwHighDateTime;
#    } FILETIME, *PFILETIME;
#
# NOTE: The lpSystemTimeAsFileTime parameter is a pointer to the above
# structure, so we'll need to pass a pointer to a FILETIME structure.
# OTOH, the GetSystemTimeAsFileTime() function has no return value, so
# we'll use the ctypes.Void pointer type.
#
# NOTE: We need to use the ctypes.Structure class to create the FILETIME
# structure.  In addition, we need to use the ctypes.Union class to create
# the LPFILETIME pointer.  We'll define both classes below.
#
# NOTE: The GetSystemTime
