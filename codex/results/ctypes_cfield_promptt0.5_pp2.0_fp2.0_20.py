import ctypes
# Test ctypes.CField
#
# This test checks that ctypes.CField subclasses can be used in
# Structures and Unions.  In particular, it checks that the
# _ctypes.CField_set method is called correctly.
#
# The CField subclass used in this test is a dummy subclass which
# simply sets its value to 42 when it is set.  The test checks that
# the value of the field is 42 after it has been set.
#
# The test also checks that a field of a Union can be set by
# assigning to a field of the Union.  This is done by defining a
# Structure and a Union, and assigning to a field of the Structure
# and checking that the value of the Union field is correct.
#
# The test also checks that a field of a Union can be set by
# assigning to a field of the Union.  This is done by defining a
# Structure and a Union, and assigning to a field of the Structure
# and checking that the value of the Union field is correct.
#
# The test also checks that a field of a Union can be set by
# assigning to the Union itself.  This
