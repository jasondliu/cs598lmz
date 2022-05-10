import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyField(ctypes.CField):
    def __init__(self, name, offset, size, type, doc):
        self.name = name
        self.offset = offset
        self.size = size
        self.type = type
        self.doc = doc

    def __repr__(self):
        return "MyField({!r}, {!r}, {!r}, {!r}, {!r})".format(
            self.name, self.offset, self.size, self.type, self.doc)


class MyStructure(ctypes.Structure):
    _fields_ = [MyField('x', 0, 4, ctypes.c_int, 'doc')]

print(MyStructure.x)
print(MyStructure())
</code>

