from _struct import Struct
s = Struct.__new__(Struct)
#                                                   12345
s._types = b"@iBcb123cb1cb12"
#                         1234567890
s._str = b"@iBcb123cb1cb12"
#                          ' '   1   ' '
#                                 ^
s._names = ("a", "i", "B", "c", "b", "1", "2", "3", "c", "b", "1", "c", "b", "1", "2")
s._count = 2
s._byteorder.__set__(s, '@') # set to native
#                               ^
try:
    s._byteorder.__set__(s, 'c');
except ValueError:
    print('ValueError')
#            ^
# ValueError

# struct_float.py
# from _struct import Struct
s = Struct.__new__(Struct)
#                                                   12345
s._types = b"@fBcb123cb1cb12"
#                         1234567890
s._str = b"@fBcb123cb1cb
