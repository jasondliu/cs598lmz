import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('p', S), ('q', S)]

d = D()

# prints <Field type=L, ofs=0>, <Field type=L, ofs=4>
for x in D._fields_:
    print x

# prints <Field type=L, ofs=4>
print getattr(D, 'q')

# prints <Field type=L, ofs=8>
print getattr(D, 'p').offset

# prints <Field type=L, ofs=0>
print getattr(D, 'q').offset

# prints <Field type=L, ofs=0>
print getattr(D, 'p')._get_offset()

# prints <Field type=L, ofs=4>
print getattr(D, 'q')._get_offset()

# prints 'wrong', of course
print getattr(D, 'p')._get_offset() + getattr(D, 'q')._get_offset()

# prints 8
print
