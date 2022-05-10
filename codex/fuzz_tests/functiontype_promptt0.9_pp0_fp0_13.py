import types
# Test types.FunctionType to distinguish user-defined functions from
# other callables like classes, instance methods and built-in functions.
# Docstring should be available in __doc__
assert issubclass ( types.FunctionType , types.Callable )
assert issubclass ( types.LambdaType   , types.FunctionType )
#============================================================
# Argument Clinic tests
#============================================================
def f_noarg ():
    __annotations__ = {
        'return' : str ,
    }

def f_posarg ( a : str ):
    __annotations__ = {
        'return' : str ,
    }


def f_vararg ( *args : str ):
    __annotations__ = {
        'return' : str ,
    }

def f_posarg_vararg ( a : str , *b : str ):
    __annotations__ = {
        'return' : str ,
    }

def f_posarg_default ( a : str , b : str = 'b' ):
    __annotations__ = {
        'return' : str ,
    }

