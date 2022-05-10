import types
# Test types.FunctionType, types.MethodType and a class
# with a __call__ method.

# create a function
def function(x):
    return x + 1

# create a method
class C(object):
    def method(self, x):
        return x + 1

# create a class with a __call__ method
class D(object):
    def __call__(self, x):
        return x + 1

# create a function with a closure
def function_closure():
    local = 1
    def closure(x):
        return x + local
    return closure

# create a method with a closure
def method_closure():
    class C(object):
        local = 1
        def closure(self, x):
            return x + self.local
    return C()

# create a __call__ method with a closure (from the above)
def call_closure():
    def __call__(self, x):
        return x + self.local
    class C(object):
        local = 1
    C.__call__ = __call__
    return C()


