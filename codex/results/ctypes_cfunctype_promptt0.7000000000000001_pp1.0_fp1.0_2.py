import ctypes
# Test ctypes.CFUNCTYPE()
# 
# Verify that functions created with CFUNCTYPE() are callable.
#
# In this example we define a function in C, then use CFUNCTYPE() to create a
# callable object from it.
#
# History:
# 2003-04-08 fl   Created
#
# Copyright (c) 2003, by Secret Labs AB
# By Fredrik Lundh
#
# Info:
# http://www.pythonware.com/library/ctypes/tutorial/ctypes-5.htm#SECTION0005100000000000000000

if os.name == 'nt':
    from ctypes import windll

    msvcrt = windll.msvcrt
else:
    import ctypes.util
    msvcrt = ctypes.CDLL(ctypes.util.find_library('c'))

message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)

# prototype of the function in "msvcrt.dll"
msvcrt.printf.argtypes = [
