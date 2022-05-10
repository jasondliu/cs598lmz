import ctypes
FUNTYPE = ctypes.CFUNCTYPE( None, ctypes.py_object, ctypes.c_int, ctypes.py_object )

"""
Purpose:
    Function to generate an event handler.
Parameters:
    param1 (in, optional) - a string, the name of the function.
    param2 (in, optional) - a list of strings, the names of the parameters.
    param3 (in, optional) - a string, the name of the return type.
    param4 (in, optional) - a string, the name of the callback function.
Return:
    The function definition.
"""
def GenerateHandler( functionName = "handler", paramList = [], returnType = "void", callbackName = "callback" ):
    paramString = ""

    for i in range( 0, len(paramList) - 1 ):
        paramString += paramList[i] + ", "
    paramString += paramList[len(paramList) - 1]

    return "void " + functionName + "( " + paramString + " ) { " + returnType + " retval = " + callbackName + "( " + paramString + "
