import ctypes
# Test ctypes.CFUNCTYPE()

# This is a bug in ctypes:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1430379&group_id=71702&atid=536732
# The following line should be:
#CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: x + y)

# But this works:
