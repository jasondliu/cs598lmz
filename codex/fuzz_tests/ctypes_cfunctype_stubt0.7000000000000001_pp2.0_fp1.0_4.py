import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World!"

# Create a class instance
class_ = ctypes.pythonapi.PyObject_GetAttrString(ctypes.py_object(MyClass),
                                                 '__dict__')['__class__']()

# Add a function to the class instance
class_.fun = fun

# Call the newly added function
print(class_.fun())
</code>
Result:
<code>Hello World!
</code>

