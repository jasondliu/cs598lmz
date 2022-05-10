import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a bit of a hack, but it lets us get the object associated with the
# exception type.
def _get_exception_type(exception):
    return ctypes.cast(id(exception), ctypes.py_object).value

def _get_exception_message(exception):
    return str(exception)

def _get_exception_traceback(exception):
    return sys.exc_info()[2]

def _is_exception_type(exception, exception_type):
    return _get_exception_type(exception) is exception_type

def _is_exception_instance(exception, exception_type):
    return isinstance(exception, exception_type)

def _get_exception_stack(exception):
    if hasattr(exception, '__traceback__'):
        return exception.__traceback__
    else:
        return sys.exc_info()[2]

