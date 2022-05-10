import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class DebugRefcounting(object):
    def __init__(self):
        self.old_ctr = ctypes.c_int.from_address
        ctypes.c_int.from_address = self.from_address

    def from_address(self, address):
        old_val = self.old_ctr(address).value
        new_val = old_val + 1
        ctypes.c_int.from_address(address).value = new_val
        print("Refcounting", address, new_val, "->", old_val)
        return old_val

    def __del__(self):
        ctypes.c_int.from_address = self.old_ctr

s = S()
a = s.x
del s
del DebugRefcounting

print(a)
