import ctypes
ctypes.cast(obj, ctypes.py_object).value

#def on_exception(type, value, trace):
#    print("My exception handler", value)
#sys.excepthook = on_exception

class LearnException(Exception):
    """
    An exception class for ReadLearn.
    To raise an exception, write:

        raise LearnException("Exception text")

    The text will be printed and the program will exit.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def path_join(p1, p2):
    """
    Checks if p2 is an absolute path, and if it is, returns it.
    Otherwise, returns the concatenation of p1 and p2.
    Both paths are passed as lists of strings representing directory names.
    """
    if p2[0] == "/":
        return p2
    else:
        return p1 + p2

def get_files(path):
    """
    Returns a list of all
