import types
# Test types.FunctionType, types.LambdaType, types.CodeType, types.
# FunctionType, builtin list, and class f1.

class A:
    '''A is just a class, with methods that do nothing.
    '''
    def __init__(self):
        pass
    def return_function(self):
        def f():
            return 'f'
        return f
    def return_lambda(self):
        return lambda : 'lambda'
    def return_str(self):
        return 'str'
    def overload_function(self):
        def g():
            return 'g'
        def f(x):
            return 'function'
        return f
    def overload_lambda(self):
        return lambda x: ('lambda', x)
    def overload_code(self):
        return types.CodeType(0, 0, 0, 0, '\n', (None, None),
                              (None, None),
                              ("the_code",),
                              "the_code.func_name", "the_code", 0,
                              "return 1
