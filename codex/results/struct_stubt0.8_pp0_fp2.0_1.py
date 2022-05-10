from _struct import Struct
s = Struct.__new__(Struct)
setattr(s, 'format', 'QQQQQQQQ')  # Pack 8 ulonglong's
setattr(s, 'size', 64)

# NOTE: This is a python2/3 hybrid file.  We're doing it because currently
# both python2 and python3 have to have an instance of this class.  Only
# python3 will actually use it to decrypt.  That's why the crazy imports.
class HostKeyEntry(object):
    r"""
    HostKeyEntry is a class used to store host keys.  It wraps the base
    key and signature data in a class that can be pickled.  It can also
    be stored in an sqlite database.

    It provides a to_blob() method that can be used to return the pickle
    data for the object.  It provides a from_blob() method that can be
    used to reconstruct the object from the pickle data.

    It provides a to_sql() method that can be used to return the sql data
    for the object.  It provides a from_sql() method that can be used to
    reconstruct the object
