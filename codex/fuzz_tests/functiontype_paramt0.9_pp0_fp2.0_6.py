from types import FunctionType
list(FunctionType(FunctionType))

# Real simple functional iterator
def FunctionalIterator():
    '''A functional version of the generator iterator.'''
    def iter(func, arg):
        def next(currFun, accum):
            '''Iterate the given function until you get an error.'''
            try:
                nextFun = currFun(accum)
            except ConvergenceError:
                raise StopIteration()
            else:
                return next(nextFun, accum+1)
        return next(func, arg)
    return iter
for _ in FunctionalIterator()(FunctionType(FunctionType), 1):
    'Foo'

###############################################################################
# function decorators

# decorate with @
def some_function():
    "Do something"
    return True
some_function = staticmethod(some_function)
del some_function


def profile_me():
    '''Do something very fast'''

@profile_me()
class A:
    pass

# decorate with @
if False:
    @profile_me
    def aFunction(aArg):

