from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda: 0, lambda x: 0))

# Test that __closure__ is copied
def f1():
    x = 3
    def f2():
        return x
    return f2

def f3():
    x = 3
    def f4():
        return x
    return f4

f2, f4 = f1(), f3()
f2.__closure__ == f4.__closure__

# Test that __closure__ is copied
def f1():
    x = 3
    def f2():
        return x
    return f2

def f3():
    x = 3
    def f4():
        return x
    return f4

f2, f4 = f1(), f3()
f2.__closure__ == f4.__closure__

# Test that __closure__ is copied
