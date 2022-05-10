import _struct
# Test _struct.Struct.__len__()

# Class:
class Struct(_struct.Struct):
    def __len__(self):
        return 1

# Instance:
class Struct2(_struct.Struct):
    pass
Struct2.__len__ = lambda self: 1

for t in 'bBhHiIlLfd':
    fmt = Struct(t)
    try:
        len(fmt)
    except TypeError:
        print(t, end='')

for t in 'bBhHiIlLfd':
    fmt = Struct2(t)
    try:
        len(fmt)
    except TypeError:
        print(t, end='')
