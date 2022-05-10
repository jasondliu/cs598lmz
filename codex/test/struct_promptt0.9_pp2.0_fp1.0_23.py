import _struct
# Test _struct.Struct

# Functions for the first version.

def stringmax(*args, **kw):
    arr = []
    for i,arg in enumerate(args):
        l = len(arg)
        m = kw.get("max",0)
        m = m + kw.get("max%d"%i,0)
        if m < l:
            m = l
        arr.append("%%%ds"%m)
    return ' '.join(arr)

def routine_v1(*args, **kw):
    s = stringmax(*args, **kw)
    f = _struct.Struct(s)
    unpack = f.unpack
    pack = f.pack
    for arg in args:
        arg = arg.ljust(len(arg)+1)
        arr = unpack(arg)
        s = pack(*arr)
        assert s == arg

# Functions for the second version.

def routine_v2(*args, **kw):
    if not args:
        args = []
        n = kw['n']
