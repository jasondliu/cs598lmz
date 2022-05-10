import ctypes
# Test ctypes.CFUNCTYPE
if isinstance(TestEnum.V1, ctypes._SimpleCData):
    print("#2 TestEnum.V1 is ctypes._SimpleCData")

if isinstance(TestEnum.V1, ctypes._CFuncPtr):
    print("#2 TestEnum.V1 is ctypes._CFuncPtr")

if isinstance(TestEnum.V1, ctypes.CFUNCTYPE):
    print("#2 TestEnum.V1 is ctypes.CFUNCTYPE")

if isinstance(TestEnum.V1, ctypes._CData):
    print("#2 TestEnum.V1 is ctypes._CData")

if isinstance(TestEnum.V1, int):
    print("#2 TestEnum.V1 is integer")

# Test memory ordering
if hasattr(TestEnum.V1, '__memory_ordering__'):
    print("#2 TestEnum.V1 has __memory_ordering__")

if hasattr(TestEnum.V2, '__memory_ordering__
