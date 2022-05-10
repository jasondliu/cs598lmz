import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

class __extend__(pairtype(SomeInteger, SomeInteger)):
    def getitem((i1, i2), index):
        if index == 0:
            return i1
        elif index == 1:
            return i2
        else:
            raise IndexError
    getitem.can_only_throw = []

class __extend__(pairtype(SomeInteger, SomeInteger)):
    def union((i1, i2)):
        if i1.unsigned == i2.unsigned:
            return SomeInteger(nonneg=i1.nonneg or i2.nonneg,
                               unsigned=i1.unsigned)
        else:
            return SomeInteger()
    union.can_only_throw = []

class __extend__(pairtype(SomeInteger, SomeInteger)):
    def add((i1, i2)):
        if i1.unsigned == i2.unsigned:
            return SomeInteger(nonneg=i1.nonneg and i2.nonneg,
                
