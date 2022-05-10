import ctypes
# Test ctypes.CFUNCTYPE

# Function prototype for first callback
CALLBACK_FUNC =  ctypes.CFUNCTYPE(None, ctypes.c_int)

def pycallback(val):
    print("pycallback(%r)" % val)

myvariant = ctypes.c_int(42)

try:
    # Try to call it first.
    # This should raise an exception because the callback
    # is not yet set
    calllback_func(myvariant)
except AttributeError:
    pass
except TypeError: # Python 3
    pass

##### Type related tests ##################

class X(object):
    pass

X_p    = ctypes.POINTER(X)
X_pp   = ctypes.POINTER(X_p)
X_ppp  = ctypes.POINTER(X_pp)
X_pppp = ctypes.POINTER(X_ppp)

for tp, arg in (
    (X, X()),
    (X_p, X_p()),
    (X_pp,
