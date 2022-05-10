from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# OUT: [<function _f at 0x7f2a03d3a730>]
# END: list_function_type()


def list_function_type_2():
    def f():
        pass
    f.__defaults__ = (1, 2, 3)
    list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# OUT: [<function _f at 0x7f2a03d3a7b8>]
# END: list_function_type_2()


def list_function_type_3():
    def f():
        pass
    f.__closure__ = (1, 2, 3)
    list(FunctionType(f.__code__, f.__globals__, name=f.__name
