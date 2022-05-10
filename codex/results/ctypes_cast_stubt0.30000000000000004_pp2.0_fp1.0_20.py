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
    
    def __call__(self, source, mode="eval", globs=None, locs=None):
        """Compile and evaluate the given source in the given mode.
        
        Parameters
        ----------
        source : str
            A string of Python source code.
        mode : str, optional
            The mode in which to compile the code.  Valid values are 'eval',
            'exec', 'single', 'eval_single', 'exec_single'.  See the
            documentation for the compile builtin function for more details.
        globs : dict,
