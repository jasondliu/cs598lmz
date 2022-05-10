fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
TypeError: 'generator' object is not callable

#}

#{
# lambda
#}

#{
import types

fn = lambda: None

print(type(fn))
print(type(fn.__code__))
print(type(fn.__code__.__class__))
print(fn.__code__.__class__ == types.CodeType)
print(fn.__code__.__class__ == types.FunctionType)
print(fn.__code__.__class__ == types.LambdaType)

print(fn.__code__.co_argcount)
print(fn.__code__.co_varnames)
print(fn.__code__.co_freevars)
print(fn.__code__.co_cellvars)

<class 'function'>
<class 'code'>
<class 'type'>
True
False
False
0
()
()
()

#}

#{
# function
#}

#{
import types

def
