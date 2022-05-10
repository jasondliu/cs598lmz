import types
# Test types.FunctionType
def _f():
    pass

def _test():
    if type(_f) == types.FunctionType:
        return func_t
