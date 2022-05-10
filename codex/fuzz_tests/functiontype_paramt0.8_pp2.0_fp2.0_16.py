from types import FunctionType
list(FunctionType(add(2, 3), globals())())

# Example 2
class derp(object):
    def __init__(self, foo, bar, baz):
        print "I'm a derp"
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def __call__(self):
        print "I'm a derp call"
        print self.foo
        print self.bar
        print self.baz

import types
def lambda_derp(foo, bar, baz):
    ret = types.FunctionType(add_func.func_code, dict(zip(add_func.func_code.co_varnames[1:], (foo, bar, baz))))
    x = lambda: ret()
    return x

derp_obj = lambda_derp(3, 5, 7)
derp_obj()

# Example 3
def myfilter(lst, func):
    for item in lst:
        if func(item):
            yield item

evens = lambda x: x % 2
