from _struct import Struct
s = Struct.__new__(Struct)
s.format = '=Ihh'
s.size = 8
s.pack(1, 2, 3)

def unpack(self, string):
    if len(string) != self.size:
        raise error
    return self.unpack_from(string)

s.unpack = unpack
s.unpack_from = Struct.unpack_from.__get__(s)
s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x03\x00')

############################
# 定义__getattr__, __setattr__, __delattr__
class Student:
    def __init__(self):
        self.name = 'Micheal'

    def __getattr__(self, item):
        if item == 'score':
            return 99

s = Student()
print(s.name)
print(s.score)

class Student:
    def __getattr__(self, item):
        if item == 'age':
            return lambda:25
