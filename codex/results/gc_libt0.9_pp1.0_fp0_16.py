import gc, weakref

class A:
    pass

def func():
    print("called")

# PyObject** objects
c_o = py_object(1)

# PyObject* objects
c_o2 = py_object(1)

# __weakref__
o = A()
wr = weakref.reference(o, func)
