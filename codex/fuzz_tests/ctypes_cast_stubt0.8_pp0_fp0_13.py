import ctypes
ctypes.cast(100, ctypes.c_float) # Cast an integer to a c_float

# =================================================================
#     find address of a parameter
# =================================================================
# get the address of a named parameter
# to use in ctypes function calls
import win32api
import win32con

def getParamAddr(func_name, parname):
    """ getParamAddr(func_name, parname) returns the
    address of parname within the win32api function func_name.
    This is useful for using ctypes to call a win32api function
    with a pointer to a structure e.g.
    SetWindowPos(handle, ptr_to_rect_struct, x, y, w, h, flags)
    where the rect_struct contains the height and width of the
    window.
    The function returns the address of parname within the
    struct e.g. rect_struct.top - the offset of the top parameter
    within the struct.

    """
    import win32api
    import win32con
    func = getattr(win32api, func_name)
    par
