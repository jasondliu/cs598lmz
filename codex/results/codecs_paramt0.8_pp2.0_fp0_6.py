import codecs
codecs.register_error('replace_python2', codecs.replace_errors)


# ----------------------------------------------------------------------

class VB2PyError(Exception):
    """Base error thrown by VB2Py"""
    pass


# ----------------------------------------------------------------------

def read_file(filename):
    """Read a file"""
    return file(filename, "rb").read()


# ----------------------------------------------------------------------

class VariableNotFound(VB2PyError):
    """Thrown when a variable is not found"""
    pass


# ----------------------------------------------------------------------

class InvalidName(VB2PyError):
    """Thrown when a variable is not found"""
    pass


# ----------------------------------------------------------------------


class Scope(object):
    """
    This is the basic scope for the VB2Py parser and is derived from the
    VBParser scope. It provides a few base functions and various settings
    for the parser
    """

    def __init__(self, _globals, _locals):
        """Constructor"""
        self._globals = _globals
        self._locals = _locals

    def handle_assignment(
            self,
