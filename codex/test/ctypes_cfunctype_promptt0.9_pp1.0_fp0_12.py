import ctypes
# Test ctypes.CFUNCTYPE
# Uncomment following line to easily show the tp_mro of CFUNCTYPE
# CFUNCTYPE.__mro__

class P: pass
class C(P): pass
class D(P): pass
class E(C, D): pass

print(E.__mro__)

