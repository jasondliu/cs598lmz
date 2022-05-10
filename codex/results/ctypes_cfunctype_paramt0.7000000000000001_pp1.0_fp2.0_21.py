import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class b2ContactListener(ctypes.Structure):
    pass

class b2Vec2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float)]

class b2AABB(ctypes.Structure):
    _fields_ = [("lowerBound", b2Vec2),
                ("upperBound", b2Vec2)]

class b2BodyDef(ctypes.Structure):
    _fields_ = [("userData", ctypes.c_void_p),
                ("position", b2Vec2),
                ("angle", ctypes.c_float),
                ("linearVelocity", b2Vec2),
                ("angularVelocity", ctypes.c_float),
                ("linearDamping", ctypes.c_float),
                ("angularDamping", ctypes.c_float),
                ("allowSleep", ctypes.c_bool),
                ("awake", ctypes.c
