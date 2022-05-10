import types
# Test types.FunctionType
# TODO: instances of types.MethodType won't have this attribute!
fn_attrs = [
        '__code__',
        '__defaults__',
        '__globals__',
        '__name__']

def fn_test(fn):
    for attr in fn_attrs:
        if not hasattr(fn,attr):
            return False
    return True
## Define a function with basic attributes
def fn1(x,y,z=0,*a,**b):
    pass
## Define a function with basic attributes and a docstring
def fn2(r):
    pass
fn2.__doc__ = '''
    Documentation for fn2
    '''

## Apply fn_test to these two functions:
print("Passed all test cases? %s"%(fn_test(fn1) and fn_test(fn2)))

## Let's see what attributes have been properly set:
for key in fn_attrs:
    print("fn1.%s == %s"%(key,getattr(fn1,key
