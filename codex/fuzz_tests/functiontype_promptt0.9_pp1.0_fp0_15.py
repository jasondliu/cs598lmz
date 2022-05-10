import types
# Test types.FunctionType
def foo(): return 10

print isinstance(foo, types.FunctionType)
print isinstance(lambda: 0, types.FunctionType)
<=>
def foo():
    return 10


class ForcePasswordChange(object):
    def __init__(self, function_to_wrap):
        self.function_to_wrap = function_to_wrap

    def __call__(self, *args):
        if True:
            print 'Welcome New User'
            return self.function_to_wrap(*args)
        else:
            print 'You need to change your password!'


@ForcePasswordChange
def first_function_to_run():
    print 'running my function'


first_function_to_run()
import itertools

a = itertools.product([1, 2], ['a', 'b'], [1.+, 2.+, 3.+])

#print a.next()
#print a.next()
for i in a:
    print i
    
import itertools as it

print 'product(A, B)', [(x,
