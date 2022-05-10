import types
# Test types.FunctionType

def func(a,b,c,d):
    print "This is a function"

def func2(a):
    print a
    print "This is a function"

print types.FunctionType(func.func_code, func.func_globals, None, None, func.func_closure)
print types.FunctionType(func.func_code, func.func_globals, "func2", func.func_defaults, func.func_closure)

try:
    types.FunctionType(func.func_code, func.func_globals, None, None)
except TypeError, e:
    print "Exception caught:",e

try:
    types.FunctionType(func.func_code, func.func_globals, "func2", (1,2,3,4,5,6))
except TypeError, e:
    print "Exception caught:",e

try:
    types.FunctionType(func.func_code, func.func_globals, "func2", (1,2,3,4,5
