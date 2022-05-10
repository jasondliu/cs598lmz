import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

class _EvalSpace(object):
    """Namespace used for evaluating python expressions.

    This class is used as a namespace for evaluating python expressions
    using the eval() function.  It is also used to provide an execution
    environment for code compiled with the compile() function.

    Class ExprSpace defines the builtins that are available to the
    code being evaluated.
    """
    __slots__ = ('__dict__', '__name__', '__doc__')

    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        object.__setattr__(self, '__dict__', dict)
        object.__setattr__(self, '__name__', 'ExprSpace')
        object.__setattr__(self, '__doc__', None)

    def __repr__(self):
        return "<ExprSpace>"

    def __getattribute__(self, name):
        if name == '__members__':
            return self.__dir__
