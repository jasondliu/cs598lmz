import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class PyFunc(ctypes.Structure):
    _fields_ = [("m_self", ctypes.py_object),
                ("m_func", FUNTYPE)]

class PyClass:
    def __init__(self):
        self.m_value = 0
    def __del__(self):
        print("del")
    def set_value(self, v):
        self.m_value = v
    def get_value(self):
        return self.m_value

def create_pyfunc(pyclass):
    pf = PyFunc()
    pf.m_self = pyclass
    pf.m_func = FUNTYPE(pyclass.get_value)
    return pf

def destroy_pyfunc(pf):
    del pf.m_self

def test():
    pc = PyClass()
    pc.set_value(99)
    pf = create_pyfunc(pc)
    print(pf.m_func
