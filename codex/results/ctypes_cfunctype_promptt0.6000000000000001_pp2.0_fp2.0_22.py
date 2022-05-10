import ctypes
# Test ctypes.CFUNCTYPE
#
# This should not crash as it did in 2.2
#
# See http://sourceforge.net/tracker/index.php?func=detail&aid=528608&group_id=5470&atid=105470

def callback(a,b): pass

n = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(callback)

# bug #528608 reported that this could cause a crash
n = None
