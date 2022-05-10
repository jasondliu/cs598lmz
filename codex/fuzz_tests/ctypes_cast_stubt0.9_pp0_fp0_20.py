import ctypes
ctypes.cast(1,1)

def py2_cast(J) : 
    """ cast to a python type

    e.g.
    py2_cast('hello' )  # returns array('c', 'hello')

    """
    return ctypes.cast(J, ctypes.py_object).value

def get_py_names(Jpy_attr_dict) : 
    """
    e.g. 
    get_py_names(JPy_attr_dict) 
    
    """
    for attr in Jpy_attr_dict : 
        yield py2_cast(attr)


def py_get_NPtypes(Jpy_NPtypes) :
    """
    """
    for Jpy in Jpy_NPtypes : 
        yield py2_cast(Jpy)


JPy_attr_dict = java.lang.String.getNames(java.lang.reflect.Array)
JPy_NPtypes = java.lang.reflect.Array._getNTypePrimitives(java.lang.reflect.Array)

def py_cast_attr(
