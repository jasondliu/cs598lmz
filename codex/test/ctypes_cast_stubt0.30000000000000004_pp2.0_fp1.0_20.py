import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

class _Evaluator(object):
    """A callable object that evaluates an expression in various ways.
    
    The public interface consists of the __call__ method and three attributes:
    symbol_table, compiler, and engine.
    """
    def __init__(self, symbol_table=None, compiler=None, engine=None):
        self.symbol_table = symbol_table
        self.compiler = compiler
        self.engine = engine
    
