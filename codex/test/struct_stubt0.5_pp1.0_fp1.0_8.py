from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(1)

# This is a bug in Python.  The problem is that the __new__ method
# of Struct is called with the Struct class as first argument.  The
# Struct class is not a subclass of Struct and therefore the
# Struct.__new__ method raises an exception.  The exception is
# caught, but the instance is not deleted.  This instance is then
# returned by the Struct.__new__ method.  The instance is unusable
# because it has no _fmt attribute.  The Struct.__init__ method then
# fails with an AttributeError.  Because the exception is not caught
# by the Struct.__new__ method, the instance is not deleted and
# therefore can be used to trigger the bug.

# This bug only exists in Python 2.4 and 2.5.  It has been fixed in
# Python 2.6.

# Fix the bug by catching the exception in the Struct.__new__ method.

# This bug is present in SimpleXMLRPCServer.py.  It is fixed in
# SimpleX
