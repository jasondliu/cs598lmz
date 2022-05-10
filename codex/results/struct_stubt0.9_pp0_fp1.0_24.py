from _struct import Struct
s = Struct.__new__(Struct)
print s
s.__init__('hhh')
print s.size
s.unpack(b'\x12\x34\x56')
d = s.unpack(bytearray(b'\x12\x34\x56'))
print d

"""
O1:
    File "..\class_struct.py", line 9, in <module>
        s = Struct.__new__(Struct)
TypeError: __new__() takes exactly 2 arguments (1 given)
O2:
    File "..\class_struct.py", line 11, in <module>
        s.__init__('hhh')
TypeError: this constructor takes no arguments
O3:
    File "..\class_struct.py", line 12, in <module>
        print s.size
AttributeError: 'Struct' object attribute 'size' is read-only
O4:
    File "..\class_struct.py", line 14, in <module>
        s.unpack(b'\x12\x34\x56')
TypeError: descriptor 'unpack
