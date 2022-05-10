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
