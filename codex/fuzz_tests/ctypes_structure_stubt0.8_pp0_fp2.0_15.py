import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)

try:
    a = S()
    print('x', a.contents.x)
    print('y', a.contents.y)
    ###NOTE###
    # a.contents.x = 10  # error: readonly
    # print('x', a.contents.x)

    b = ctypes.pointer(a)
    print('b', b.contents.x)
    b.contents.x = 10
    print('b', b.contents.x)
    print('a', a.contents.x)
    ###NOTE###
    # b.contents.x = 20  # error: readonly
    # print('b', b.contents.x)

    c = ctypes.pointer(a)  # copy
    print('c', c.contents.x)
    c.contents.x = 20
    print('c', c.contents.x)
    print('a', a.contents.x)
   
