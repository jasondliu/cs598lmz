import ctypes
ctypes.cast(0, ctypes.py_object)
 
# outputs <PyCObject at 0x400139f0>

def bar():
    ctypes.cast(0, ctypes.py_object)
    return 'bar'

class CpythonImplementationDetails:
    pass

# the following does not work:
if ctypes.cast(0, ctypes.py_object).__class__ is CpythonImplementationDetails:
    print "The interpreter really is CPython!"
else:
    print "This could be CPython, or it could be anything..."


## but the following works:
if bar.func_code.co_flags & 0x20:
    print "The interpreter is CPython!"
else:
    print "This could be CPython, or it could be anything..."

# If the file of the module has been compiled, it is the same as the __file__
# module attribute.
# If it has not been compiled (i.e. it’s loaded from the source file) then the
# interpreter variable co_filename is set to this.
# Refer to the CPython source
