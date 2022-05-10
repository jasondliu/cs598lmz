import ctypes
ctypes.cast(0, ctypes.py_object).value = 0

sys.exitfunc = exitfunc   # Define at the top, assign at the bottom.
try:
    import __builtin__
    setattr(__builtin__, 'quit', exitfunc)
except ImportError:
    import builtins
    setattr(builtins, 'quit', exitfunc)

# Assign different exitcodes depending on the result of the tests.
if __name__ == '__main__':
    sys.exitfunc()
