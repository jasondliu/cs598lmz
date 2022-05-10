import ctypes
# Test ctypes.CFUNCTYPE
def mesh_set_joint_method(self,integration_method,joint):
    print "Success setting joint method for mesh"

def mesh_get_joint_method(self,integration_method,joint):
    print "Success getting joint method for mesh"

Mesh = ctypes.CFUNCTYPE(None,ctypes.c_char_p,ctypes.c_void_p)

# Test ctypes.Struct
class Vertex(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double),
                ("z", ctypes.c_double), ("color", ctypes.c_long)]

Vertex_STORAGE_TYPE = ctypes.POINTER(Vertex)


# Test ctypes.CFUNCTYPE(None,[ctypes.c_long_p])
def compute_distance(x, y):
    return x+y

CallBackFunc = ctypes.CFUNCTYPE(None, ctypes.c_long, ctypes.c
