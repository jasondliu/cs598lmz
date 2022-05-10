from _struct import Struct
s = Struct.__new__(Struct)
print(s)

class SubStruct(Struct):
    def __new__(cls, *args, **kwargs):
        print('Substruct __new__')
        return Struct.__new__(cls, *args, **kwargs)

SubStruct.mro()
s = SubStruct()
s = SubStruct.__new__(SubStruct)
print(s)

class SubStructWithoutNew(Struct):
    pass

s = SubStructWithoutNew()
