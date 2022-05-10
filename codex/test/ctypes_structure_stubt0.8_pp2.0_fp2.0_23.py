import ctypes

class S(ctypes.Structure):
    x = 1,2

s = S()

ctypes.string_at(id(s))

# c:\dev\py3\lib\ctypes\__init__.py in _ctypes_from_address(address)
#    551     # Try to guess the size of the structure
#    552     size = sys.getsizeof(obj)
# --> 553     fields = cast(address, POINTER(type * size)).contents
#    554     for field, value in fields._asdict().items():
#    555         setattr(obj, field, value)
#
# ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention

dir(ctypes)
dir(ctypes.__version__)

help(ctypes.string_at)

ctypes.string_at.__doc__
