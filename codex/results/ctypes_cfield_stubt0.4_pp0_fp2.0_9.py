import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(descr, func, arg):
    print descr
    print func(arg)
    print

test("int", ctypes.CField.from_address, id(S.x))
test("str", ctypes.CField.from_address, id(S.x.__doc__))
test("int", ctypes.CField.from_address, id(S.x.__doc__))
</code>
Output:
<code>int
&lt;Field type=c_int, ofs=0, size=4&gt;

str
&lt;Field type=c_char_Array_256, ofs=0, size=256&gt;

int
&lt;Field type=c_char_Array_256, ofs=0, size=256&gt;
</code>

