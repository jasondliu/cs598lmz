from _struct import Struct
s = Struct.__new__(Struct)
s.format = Struct.format
s.format = pack;s.format = s.format;s.format

s = Struct.__new__(Struct)
s.format = Struct.format
s.format = pack;s.format();exec(s)


def L(n):
    if n is None:
        yield None
        return
    for d in L(n.left):
        yield d
    yield n
    for d in L(n.right):
        yield d

def R(n):
    if n is None:
        yield None
        return
    for d in L(n.right):
        yield d
    yield n
    for d in L(n.left):
        yield d

def T(n):
    if n is None:
        yield n
        return
    x = n
    while x.right is not None: x = x.right
    while x is not None: yield x; x = x.left
    x = n.left
