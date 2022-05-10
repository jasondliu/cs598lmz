import _struct
# Test _struct.Struct
import copy
import _testcapi
d = _testcapi.calcsize_example_configs()
def fn(obj, a0, a1, a2, a3, a4, a5, a6, a7):
    obj.__parse(a0, a1, a2, a3, a4, a5, a6, a7)
def check(t, s, *args):
    # test packing and unpacking
    b = t.pack(*args)
    args2 = t.unpack(b)
    print(s, end=" => ")
    print(args2)
    # test in-place update
    args3 = [copy.copy(a) for a in args]
    b = t.pack_into(b, 0, *args3)
    for i in range(len(args3)):
        args3[i] = copy.copy(args3[i])
    args3[:] = t.unpack_from(b, 0)
    print(s, end=" [i]=> ")
