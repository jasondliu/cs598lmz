fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn, gi

class __lambda_args:
    def __init__(self, args):
        self.args = args

def _add_lambda_arg(arg):          # For adding a single argument to a lambda
    return __lambda_args((arg,))   # function.

def _add_lambda_args(args):        # For adding multiple arguments to a lambda
    return __lambda_args(args)     # function.

# ----------------------- temporary, don't forget to remove this -----------------------

# Recover the pure-Python code for a Python function using the
# code module.  This function is necessary, because the function
# object's __code__ attribute is not accessible in restricted mode.
#
# This function is called from the inspect module.

def getsourcelines(func):
    import types, string, tokenize

    if type(func) is types.ClassType:
        lines, lnum = inspect.findsource(func)
    elif hasattr(func, 'im_func'):
        lines, lnum = inspect.findsource(func.im_func
