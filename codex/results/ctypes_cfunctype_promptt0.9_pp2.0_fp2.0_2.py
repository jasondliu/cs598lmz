import ctypes
# Test ctypes.CFUNCTYPE
#
# Origin: 
# https://docs.python.org/2/library/ctypes.html#ctypes._FuncPtr 
#
# 2017-03-03:
#
# Tested on:
# - Python 2.7.10, LLVM clang-900.0.38, x86_64, Darwin 
#
#
# NOTE: 
# Some platforms only support "name mangling", which means the 
# function name may have the argument types attached.
#
# try: 
#   libc = ctypes.CDLL(None)
#   res = libc.strcspn(b'spam', b'xyz')
# except ValueError as e:
#   print e
#   print "Try appending argument types to function names like this:" 
#   res = libc.strcspn(b'spam', b'xyz', ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)
#

c_int = ctypes.c_int
c_char_
