import ctypes
ctypes.cast(1024, ctypes.py_object).value
#2.7 output: 1024
#3.7 output: b'\x00\x00\x00\x00\x00\x00\x00\x00'

#Possible criticisms:
# 1. With some rare exceptions, the types should be const, even if
#    in C++ that might make it harder to write correct code.  In
#    my experience, writing this kind of type is largely a code
#    generation task anyway, so const would be no hardship.
#    The C++ RPC may require non-const, but that is arguable.
# 2. There is no freeing (currently) of allocated memory when the
#    RPC is finished.  I haven't looked into this, but it seems
#    like some kind of garbage collection would work here.
# 3. It would be nice to use the C++ types with python argparse
#    (and at least in principle, python ctypes), but ctypes needs
#    to be able to find the size of the data, which is hard to do
#    with C++ templates.
# 4
