import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class G(ctypes.Structure):
    pass

ctypes.CFieldType = type(G._fields_)

class P(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]
ctypes.CFieldType.__len__(P._fields_)

P._fields_

P._fields_[0]

type(P._fields_[0])

type(P._fields_[0][0])

P._fields_[0][0]

P._fields_[0][1]

P._fields_[0][1].__name__

type(P._fields_[0][1])

P._fields_[0][1]

P._fields_[0][1]

P._fields_[0][1]

P._fields_[0][1]

P._fields_[0][1]

