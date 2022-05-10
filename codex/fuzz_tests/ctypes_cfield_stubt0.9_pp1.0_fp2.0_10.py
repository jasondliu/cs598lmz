import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)  # redundant attributes
ctypes.Structure.__basestruct__ = S
ctypes.Union.__basestruct__ = S
ctypes.CField.__basestruct__ = S

import ctypes, os, sys

curr_module = sys.modules[__name__]
for typ, cls, cfunc, init in [('c_byte', 1, ctypes.c_byte, 'bytes = (1,)'),
                              ('c_short', 1, ctypes.c_short, 'shorts = (1,)'),
                              ('c_int', 1, ctypes.c_int, 'ints = (1,)'),
                          ]:
    for sizeof, signed in [(1, False), (1, True), (2, False), (2, True), (4, False), (4, True)]:
        if not signed and sizeof < 4:
            continue
        name = 'c_' + typ
        if sizeof != 1 or signed:
            name += '%d' % (8*sizeof, )
            if not signed:
                name += '_
