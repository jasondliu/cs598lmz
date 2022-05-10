import ctypes
# Test ctypes.CField
if hasattr(ctypes, "CField"):
    class X(ctypes.Structure):
        pass
    X._fields_ = [
        ('a', ctypes.CField)
    ]
    x = X()
    x.a = 1
    x.a = 2
    assert x.a == 2
else:
    print("SKIP")
    raise SystemExit

# Test ctypes.CField with field name
if hasattr(ctypes, "CField"):
    class X(ctypes.Structure):
        pass
    X._fields_ = [
        ('a', ctypes.CField('b'))
    ]
    x = X()
    x.a = 1
    x.a = 2
    assert x.a == 2
else:
    print("SKIP")
    raise SystemExit

# Test ctypes.CField with offset
if hasattr(ctypes, "CField"):
    class X(ctypes.Structure):
        pass
    X._fields_ = [
        ('a', ctypes.CField(
