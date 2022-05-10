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
