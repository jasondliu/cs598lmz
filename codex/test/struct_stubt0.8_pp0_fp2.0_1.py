from _struct import Struct
s = Struct.__new__(Struct)
setattr(s, 'format', 'QQQQQQQQ')  # Pack 8 ulonglong's
setattr(s, 'size', 64)

# NOTE: This is a python2/3 hybrid file.  We're doing it because currently
# both python2 and python3 have to have an instance of this class.  Only
# python3 will actually use it to decrypt.  That's why the crazy imports.
