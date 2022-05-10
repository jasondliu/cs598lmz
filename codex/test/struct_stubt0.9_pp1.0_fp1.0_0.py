from _struct import Struct
s = Struct.__new__(Struct)
s.init_types(b'c',b'I')
InitialHead = s.build
Head = Struct.__new__(Struct)
Head.init_types(b'H',b'I')
print(s)
print(Head)
# <_struct.Struct object at 0x7f03c75b3ca0>
# <_struct.Struct object at 0x7f03c75b3d90>
print(type(s))
print(type(Head))
# <class '_struct.Struct'>
# <class '_struct.Struct'>

#print(s == Head)
#print(s is Head)
#print(Head.format == s.format)
# False
# False
# False
#print(Head.format)
#IH
#print(s.format)
#cI

# 既然是继承，那么，父类的init_types被子类覆盖了，父类的build
