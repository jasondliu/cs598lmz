import ctypes
# Test ctypes.CFUNCTYPE

# When this is run as a standalone program, we get the following error:
#    Traceback (most recent call last):
#      File "cfuntype.py", line 4, in <module>
#        @CFUNCTYPE(c_int, c_int)
#    NameError: name 'CFUNTYPE' is not defined
#
# When this is run using 'python -m test.support', it does not.

@CFUNTYPE(c_int, c_int)
def foo(n):
    p
