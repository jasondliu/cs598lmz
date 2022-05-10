import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
@FUNTYPE
def py_add_pymesh_prog_name(arg1, arg2=None):
    """
    Add progress name to pymesh progress logger.
    """
    assert(arg2 != None)
    assert(isinstance(arg2, ctypes.c_char_p))
    ProgressLogger.add_pymesh_prog_name(arg1, arg2.value)

def py_set_pymesh_prog_msg(arg1, arg2=None):
    """
    Set progress message of the current pymesh progress.  Accepts both
    str and bytes.
    """
    assert(arg2 != None)

    if(sys.version_info[0] >= 3):
        msg = arg2.decode("utf-8")
    else:
        if(isinstance(arg2, ctypes.c_char_p)):
            msg = arg2.value
        else:
            assert(isinstance(arg2, str))
            msg = arg2
    ProgressLogger.set_pym
