import ctypes
# Test ctypes.CField.__get__()
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

s = S()
print(s.a)
print(S.a.__get__(s))
print(S.a.__get__(None, S))
S.a = 50
print(s.a)
print(S.a)
print(ctypes.c_int.__get__(None, S))
print(ctypes.c_int.__get__(s))
############################################################
#
#  $ python3 test2.py
#  0
#  0
#  <field 'a' of 'S' objects>
#  50
#  <attribute 'a' of 'S' objects>
#  <class 'ctypes.c_int'>
#  50
#
