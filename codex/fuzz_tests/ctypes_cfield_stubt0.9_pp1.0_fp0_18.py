import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# ctypes.Field is the same as ctypes.CField

s = S()
print('S.x.__repr__(): ' + S.x.__repr__())
print('S.x.__str__(): ' + S.x.__str__())
print('')

ctypes.Cast = type(ctypes.byref)

# ctypes.CData is the same as ctypes.Cast

print('ctypes.byref(s).__repr__(): ' + ctypes.byref(s).__repr__())
print('ctypes.byref(s).__str__(): ' + ctypes.byref(s).__str__())
</code>
Output:
<code>S.x.__repr__(): CField('x', c_int, &lt;Field type=c_int, ofs=0, size=4&gt;)
S.x.__str__(): &lt;Field type=c_int, ofs=0, size=4&gt;

ctypes.byref(s).__
