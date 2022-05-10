import types
types.MethodType(foo, 1)

def foo(self, x):
    return x

types.MethodType(foo, 1, int)

# from https://docs.python.org/3/library/types.html
def make_counter():
    count = [0]
    def counter():
        count[0] += 1
        return count[0]
    return counter

ct = make_counter()
ct()
ct()
ct()

import types
ct2 = types.FunctionType(ct.__code__, ct.__globals__, name=ct.__name__,
                          argdefs=ct.__defaults__,
                          closure=ct.__closure__)

ct2()
ct2()
ct2()
