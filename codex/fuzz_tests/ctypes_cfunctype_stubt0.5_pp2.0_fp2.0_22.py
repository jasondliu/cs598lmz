import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# Create a new instance of the PythonInterpreter class.
# This will automatically call Py_Initialize()
interp = PythonInterpreter()

# This will automatically call Py_Finalize()
# when the interpreter goes out of scope
with interp:
    # Get the PyObject for the module
    my_module = interp.get_module("my_module")

    # Set the value of a variable in the module
    my_module.set_var("var1", "value1")

    # Get the value of a variable in the module
    var1 = my_module.get_var("var1")

    # Execute a statement in the module
    my_module.exec_statement("var2 = 'value2'")

    # Get the value of a variable in the module
    var2 = my_module.get_var("var2")

    # Call a function in the module
    result = my_module.call_function("fun1", "argument")

    # Call a function in the module and get the exception,
    # if any
    result
