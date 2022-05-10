import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

assert issubclass(ctypes.c_int, ctypes.CField)
assert not issubclass(ctypes.c_int, ctypes.Structure)
assert not issubclass(ctypes.c_int, ctypes.Union)


# Auxiliary code to test the (co)recursion depth
import os
MAX_CO = 0

def report(s, co, op="", count=0):
    try:
        global MAX_CO
        count += 1
        if s.f is None:
            return count
        else:
            assert s.f.f is s
            return report(s.f, co, "co" if op else "rec", count)
    except RecursionError:
        if count > MAX_CO:
            MAX_CO = count
            print("", MAX_CO, "...", end=""),
        return count

class OCTets(BITS_types):
    _type_ = "16s"
    def co(self):
        value = self.get()
        return OCTets(value + b'\x00')
