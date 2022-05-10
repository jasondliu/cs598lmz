import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    for cls in (S.x,):
        for x in cls._get_type_() ::
            x.c_subtype, 'subtype'
        for x in cls.c_subtype ::
            x.subtype, 'subtype'
        for x in cls.subtype ::
            x.subtype, 'subtype'
        for x in cls.subtype._get_type_() ::
            x.subtype, 'subtype'
        for x in cls.subtype.subtype ::
            x.subtype, 'subtype'

import sys
sys.path[0] = sys.path[0] + '/../Python-2.7.2'
main()
</code>

